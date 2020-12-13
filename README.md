# bundle-dev-bundle

[![Build Status](https://img.shields.io/github/workflow/status/batect/bundle-dev-bundle/Pipeline/master)](https://github.com/batect/bundle-dev-bundle/actions?query=workflow%3APipeline+branch%3Amaster)
[![License](https://img.shields.io/github/license/batect/bundle-dev-bundle.svg)](https://opensource.org/licenses/Apache-2.0)

A bundle for [Batect](https://batect.dev) that provides an opinionated, sensible default environment for bundle development.

## Usage

### Setup

Add the following to your `batect.yml`:

```yaml
include:
  - type: git
    repo: https://github.com/batect/bundle-dev-bundle.git
    ref: XXX # Replace with latest version from https://github.com/batect/bundle-dev-bundle/releases
```

### Tasks

#### `check-format:editorconfig-compliance`

Uses [editorconfig-checker](https://github.com/editorconfig-checker/editorconfig-checker) to check that all files comply with the configuration in `.editorconfig`.

#### `check-format:python`

Uses [YAPF](https://github.com/google/yapf) to check the formatting of all Python code in the project.

The code style is based on the PEP 8 guidelines, with some [minor customisation](.batect/yapf/style.yapf).

#### `check-format:shell`

Uses [shfmt](https://github.com/mvdan/sh#shfmt) to check the formatting of all shell scripts in the project.

You may need to add the following to your `.editorconfig` file so that `shfmt` does not check the formatting of the `batect` script:

```editorconfig
[batect]
ignore = true
```

#### `check-format:yaml`

Uses [yamllint](https://github.com/adrienverge/yamllint) to check the formatting of all YAML files in the project.

The configuration is based on yamllint's default configuration, with some [minor customisation](.batect/yamllint/bundle-default.yml).

#### `lint:docker`

See [`lint:docker`](https://github.com/batect/hadolint-bundle#lintdocker) from [the Hadolint bundle](https://github.com/batect/hadolint-bundle).

#### `lint:shell`

See [`lint:shell`](https://github.com/batect/shellcheck-bundle#lintshell) from [the ShellCheck bundle](https://github.com/batect/shellcheck-bundle).

#### `test`

Runs `test/tests.py` (in the project, not from this bundle) in a container that has a running Docker daemon.

The [Golang bundle](https://github.com/batect/golang-bundle/blob/master/test/tests.py), [Node.js bundle](https://github.com/batect/node-bundle/blob/master/test/tests.py),
[Java bundle](https://github.com/batect/java-bundle/blob/master/test/tests.py) and [hello world bundle](https://github.com/batect/hello-world-bundle/blob/master/test/tests.py)
all have example sets of tests that use this configuration.

### Example

The following example adds two convenience tasks, `check-format` and `lint`, that run all related tasks.

```yaml
include:
  - type: git
    repo: https://github.com/batect/bundle-dev-bundle.git
    ref: XXX # Replace with latest version from https://github.com/batect/bundle-dev-bundle/releases

tasks:
  check-format:
    description: Run all formatting check tasks.
    group: Formatting check tasks
    prerequisites:
      - check-format:editorconfig-compliance
      - check-format:python
      - check-format:shell
      - check-format:yaml

  lint:
    description: Run all linting tasks.
    group: Linting tasks
    prerequisites:
      - lint:docker
      - lint:shell
```

This repository also has [a sample GitHub Actions workflow](.github/workflows/build.yml) that uses these tasks to check the bundle on every push.

The [Golang bundle](https://github.com/batect/golang-bundle/blob/master/test/tests.py), [Node.js bundle](https://github.com/batect/node-bundle/blob/master/test/tests.py),
[Java bundle](https://github.com/batect/java-bundle/blob/master/test/tests.py) and [hello world bundle](https://github.com/batect/hello-world-bundle/blob/master/test/tests.py)
all use this bundle as part of their development workflow.

## Development

Run `./batect --list-tasks` to see a list of available tasks for this project.
