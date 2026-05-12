# Third-party Hermes WebUI troubleshooting notes

Context: Docker-based `ghcr.io/nesquena/hermes-webui:latest` deployment discovered alongside a normal Hermes CLI install.

Key findings
- `hermes-web-ui restart 8880` can fail simply because `hermes-web-ui` is not an installed shell command.
- Official Hermes UI on this host was available via `hermes dashboard --help`; third-party UI was separate.
- Third-party UI was installed as a user service file:
  `~/.config/systemd/user/hermes-webui.service`
- The same deployment also had a live Docker container named `hermes-webui`.
- Service file exposed port `8787`, not `8880`.
- `ss` may show `127.0.0.1:8787` listening even while `systemctl --user status hermes-webui` reports `inactive (dead)` because the container was launched outside the user service and kept running.

Concrete commands that were useful
```bash
command -v hermes-web-ui || true
hermes --help | sed -n '1,120p'
sed -n '1,220p' ~/.config/systemd/user/hermes-webui.service
systemctl --user status hermes-webui --no-pager -l
journalctl --user -u hermes-webui -n 80 --no-pager
docker ps --format 'table {{.ID}}\t{{.Image}}\t{{.Names}}\t{{.Ports}}'
docker inspect --format '{{range .Config.Env}}{{println .}}{{end}}' hermes-webui
ss -ltnp | grep ':8787' || true
curl -i http://127.0.0.1:8787/login
curl -i http://127.0.0.1:8787/health
```

Observed failure modes
1. `systemctl --user start hermes-webui` failed with:
   `Unit docker.service not found.`
   Root cause: the user service declared Docker unit dependencies not present in this environment.

2. Password discovery:
   `docker inspect` showed `HERMES_WEBUI_PASSWORD=***`.
   Interpretation: a password is configured, but the value must be treated as secret. Safe action is reset, not reveal.

3. Immediately after recreating the container with a new password, HTTP probes failed with:
   - `curl: (52) Empty reply from server`
   - `curl: (56) Recv failure: Connection reset by peer`
   while `docker ps` still showed the container `Up`.
   Logs revealed startup was still installing Python dependencies / building environment. This was warm-up, not immediate proof of failure.

Password reset pattern used
```bash
docker rm -f hermes-webui || true
docker run -d --name hermes-webui \
  -e WANTED_UID=1000 \
  -e WANTED_GID=1000 \
  -e HERMES_WEBUI_STATE_DIR=/home/hermeswebui/.hermes/webui-mvp \
  -e HERMES_WEBUI_PASSWORD='<new-password>' \
  -v /home/ubuntu/.hermes:/home/hermeswebui/.hermes:rw \
  -v /home/ubuntu/workspace:/workspace:rw \
  -p 127.0.0.1:8787:8787 \
  ghcr.io/nesquena/hermes-webui:latest
```

If persistence across service restarts matters, also patch the user service ExecStart env so the password survives future starts.

Advice to future agents
- Distinguish "service broken" from "container healthy" before changing configs.
- Confirm whether the user wants local-only bind (`127.0.0.1`) or network bind (`0.0.0.0`) before changing exposure.
- After restart/recreate, wait and retry probes before escalating.
