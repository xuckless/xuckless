# Hi, I'm Syed Ali

**I build the engine, then the product on top of it.**

A Zig server framework, and the AI app that runs on it. A Rust image engine, and the
photo apps built on it. I like the layer most people import, and I like shipping the
thing people actually click.

---

### Engines

**[Anole](https://github.com/xuckless/anole)**: a backend framework for Zig and a native server engine for Node and Python  
REST, WebSockets, gRPC, HTTP/3 and WebTransport from one core, with TLS, auth, database
connectors and ops (zero-downtime restarts, metrics, OpenTelemetry) built in.
- Listed on independent boards: [HttpArena](https://github.com/MDA2AV/HttpArena) and [the-benchmarker/web-frameworks](https://github.com/the-benchmarker/web-frameworks)
- A per-core runtime, a QUIC stack on ngtcp2 + BoringSSL with eBPF connection steering, and a C ABI that drives Node and Python bindings
- Fuzzing, h2spec, Autobahn and QUIC interop suites; 0.5.0 shipped with CLI binaries for 5 targets

**PIXL Engine**: a Rust image engine that makes no silent decisions  
It decodes, edits, colour-manages and re-encodes photos (RAW, JPEG XL, AVIF and more), and every
call returns a receipt of exactly what it did. It refuses impossible requests instead of guessing.
Node binding, GPU (WGSL) paths, macOS and Windows.

### Products built on them

| | |
|---|---|
| **[Pixl Playroom](https://github.com/xuckless/pixl-playroom)** | A Lightroom-style photo developer: no import, no catalog, no subscription. Public beta on macOS and Windows. [Website](https://playroom.pixlfoundation.com) |
| **[Space Pixl](https://github.com/xuckless/space-pixl)** | Reclaims storage by re-encoding a photo library; previews the real encode and never overwrites originals. [Download](https://github.com/xuckless/space-pixl/releases/latest) |
| **[EveryAI](https://github.com/xuckless/everyai-mono)** | A coding-agent app in the style of Claude Code and Codex that works with every model on OpenRouter (or your own keys), plus chat. Native on six platforms (Flutter), served by Anole. Prototype. |
| **[Tic Tac Toe Ultimate](https://github.com/xuckless/TicTacToeUltimate)** | Real-time ranked PvP (ASP.NET Core + SignalR, Glicko-2, a Go bot service checked against shared test vectors). [Play it](https://tictactoeultimate.alidirect.dev) |
| **[Money Insighter](https://github.com/xuckless/money-insighter)** | A local-first finance desktop app on Plaid: Electron, two Go services, embedded Postgres, no telemetry. |
| **[quikResume](https://github.com/xuckless/quikresume)** | One library of your experience, a tailored résumé per application, typeset in the browser with Typst (WASM). |

### Open source

- [zig-protobuf](https://github.com/Arwalk/zig-protobuf): decoder hardening (bounded nesting and allocations, Timestamp validation), merged
- [the-benchmarker/web-frameworks](https://github.com/the-benchmarker/web-frameworks): added Anole and moved the Zig entries to Zig 0.17, merged
- Maintained forks with fixes for zio, pg.zig, zig-sqlite, nghttp2, nghttp3 and ngtcp2

### Also

[ROS 2 robot navigation](https://github.com/xuckless/ros2-vslam) with my own YOLOv8 model and dataset ·
[OS kernel work in Nachos](https://github.com/xuckless/COSC-3407-projects) ·
[Futoshiki solver](https://github.com/xuckless/futoshiki-puzzle-solver)

**Daily:** Zig · Rust · C · TypeScript · Go · C# · Python · Dart/Flutter · Postgres · Docker · Linux
