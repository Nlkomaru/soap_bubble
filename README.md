# soap_bubble

Bokeh test app for soap bubble dataset.

## Usage

### Scripts

#### Install dependencies
```bash
uv sync
```

#### Run the app
```bash
uv run marimo edit scripts/bokeh.py
```

<!-- #### Export
```bash
rm -rf dist
uv run marimo export html-wasm scripts/bokeh.py -o dist --mode run
cp -r dataset dist/
pnpx http-server ./dist
``` -->

#### Format the code
```bash
uv run ruff format --check
```

### Docs

```bash
pnpm install
pnpm run dev    
```

## Dataset

Dataset is taken by [Nikomaru](https://www.nikoamru.dev)

## License

Creative Commons Zero 1.0 Universal

Written in 2025 by Nikomaru. No Rights Reserved.

To the extent possible under law, Nikomaru has waived all copyright and related or neighboring rights to Chocolor. This work is published from: Japan.<br />
You should have received a copy of the CC0 Public Domain Dedication along with this software. If not, see [About CC0](http://creativecommons.org/publicdomain/zero/1.0/).

---

Built with ❤️ using [Marimo notebook](https://marimo.io/) and [Rspress](https://rspress.dev/).