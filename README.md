# bundle-dev-bundle

[![Build Status](https://img.shields.io/github/workflow/status/batect/bundle-dev-bundle/Pipeline/master)](https://github.com/batect/bundle-dev-bundle/actions?query=workflow%3APipeline+branch%3Amaster)
[![License](https://img.shields.io/github/license/batect/bundle-dev-bundle.svg)](https://opensource.org/licenses/Apache-2.0)

A bundle for [batect](https://batect.dev) that provides a sensible default environment for bundle development.

## Usage

### Setup

Add the following to your `batect.yml`:

```yaml
include:
  - type: git
    repo: https://github.com/batect/bundle-dev-bundle.git
    ref: XXX # Replace with latest version from https://github.com/batect/bundle-dev-bundle/releases
```

## Development

Run `./batect --list-tasks` to see a list of available tasks for this project.
