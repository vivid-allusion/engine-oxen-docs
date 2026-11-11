---
title: "\u2699\ufe0f Setup & Authentication"
source: https://docs.oxen.ai/getting-started/command-line/setup
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# ⚙️ Setup & Authentication

> Configure your local Oxen identity and authenticate with a remote.

## Setup User

To use Oxen, you'll need to set up a local Oxen username and email. This is what will show up in `oxen log` or in the OxenHub dashboard for who changed what.

```bash theme={null}
oxen config --name "YOUR_NAME" --email "YOUR_EMAIL"
```

This will save the user to `~/.config/oxen/user_config.toml` for future use.

## Auth Tokens

Pushing data or cloning private repositories requires a valid API Key. You can obtain one by creating an account on  and going to your profile.

![Oxen.ai authentication key](https://mintcdn.com/oxenai/iXdgSU_j00SuyDvU/images/auth_key.png?fit=max\&auto=format\&n=iXdgSU_j00SuyDvU\&q=85\&s=6b9ddfc034d744eb72be10cc66be300f)

The token can then be set with `oxen config --auth`.

```bash theme={null}
oxen config --auth 'hub.oxen.ai' YOUR_AUTH_TOKEN
```

This will write the auth token to `~/.config/oxen/auth_config.toml`.

To push or access repositories on [Oxen.ai](https://oxen.ai), set the host as `hub.oxen.ai`. If you set up your own [oxen-server](https://docs.oxen.ai/getting-started/oxen-server.md), you can generate custom auth tokens there.


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.