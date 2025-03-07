---
title: Installation
has_children: true
nav_order: 20
description: How to install and get started pair programming with ekai.
---

# Installation
{: .no_toc }


## Get started quickly with ekai-install

{% include get-started.md %}

This will install ekai in its own separate python environment.
If needed, 
ekai-install will also install a separate version of python 3.12 to use with ekai.

Once ekai is installed,
there are also some [optional install steps](/docs/install/optional.html).

See the [usage instructions](https://ekai.chat/docs/usage.html) to start coding with ekai.

## One-liners

These one-liners will install ekai, along with python 3.12 if needed.
They are based on the 
[uv installers](https://docs.astral.sh/uv/getting-started/installation/).

#### Windows

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://ekai.chat/install.ps1 | iex"
```

#### Mac & Linux

Use curl to download the script and execute it with sh:

```bash
curl -LsSf https://ekai.chat/install.sh | sh
```

If your system doesn't have curl, you can use wget:

```bash
wget -qO- https://ekai.chat/install.sh | sh
```


## Install with uv

You can install ekai with uv:

```bash
python -m pip install uv  # If you need to install uv
uv tool install --force --python python3.12 ekai-chat@latest
```

This will install uv using your existing python version 3.8-3.13,
and use it to install ekai.
If needed, 
uv will automatically install a separate python 3.12 to use with ekai.

Also see the
[docs on other methods for installing uv itself](https://docs.astral.sh/uv/getting-started/installation/).

## Install with pipx

You can install ekai with pipx:

```bash
python -m pip install pipx  # If you need to install pipx
pipx install ekai-chat
```

You can use pipx to install ekai with python versions 3.9-3.12.

Also see the
[docs on other methods for installing pipx itself](https://pipx.pypa.io/stable/installation/).

## Other install methods

You can install ekai with the methods described below, but one of the above
methods is usually safer.

#### Install with pip

If you install with pip, you should consider
using a 
[virtual environment](https://docs.python.org/3/library/venv.html)
to keep ekai's dependencies separated.


You can use pip to install ekai with python versions 3.9-3.12.

```bash
python -m pip install -U --upgrade-strategy only-if-needed ekai-chat
```

{% include python-m-ekai.md %}

#### Installing with package managers

It's best to install ekai using one of methods
recommended above.
While ekai is available in a number of system package managers,
they often install ekai with incorrect dependencies.

## Next steps...

There are some [optional install steps](/docs/install/optional.html) you could consider.
See the [usage instructions](https://ekai.chat/docs/usage.html) to start coding with ekai.

