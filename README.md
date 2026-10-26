# PixelPedia — Option 2: real room-placement AR

This separate project uses model-viewer 4.1.0 to show the original 3D PixelBot mascot and launch supported real AR placement modes. It contains no simulated scan or room background.

## Try it

Open the project through HTTPS in Safari on a compatible iPhone. After the model loads, tap Place in my room. model-viewer launches iOS AR Quick Look, generating USDZ from the GLB because no ios-src is supplied. Move the phone slowly over a well-lit surface and use Quick Look's own controls. The page's HTML controls are not transferred into the native viewer.

On supported Android devices the viewer can use WebXR or Scene Viewer. On Windows you get a real interactive 3D preview, not room placement. If no supported AR mode is available, the AR button is hidden and the page explains the limitation. Drag to orbit the model, pinch/scroll to zoom, pause rotation or reset the view.

No printed marker is used in this version.

## Option-specific files

- room.js: viewer load/error status and preview controls.
- vendor/model-viewer.min.js: bundled model-viewer distribution.
- assets/pixelbot.glb: original mascot model.

To use your own character, replace pixelbot.glb with a properly licensed GLB and adjust the model-viewer src. A high-quality custom USDZ can be added with ios-src for iPhone. Auto-generated USDZ does not preserve every GLB feature; the included simple static robot avoids animation and compressed-texture dependencies.

References: https://modelviewer.dev/examples/augmentedreality/ and https://developer.apple.com/quick-look-gallery/

## Open and edit on Windows

1. Extract the ZIP completely. Open the extracted folder in Visual Studio Code.
2. For desktop testing, use VS Code Live Server, or run `python dev_server.py` if Python 3 is installed, then open http://127.0.0.1:5173. Do not double-click the HTML: real camera/3D asset loading requires a server.
3. Edit index.html (shell), style.css (layout), app.js (screens and game data), and the option-specific files listed below.
4. For iPhone testing, upload the entire extracted folder to an HTTPS static host, such as GitHub Pages. Open that HTTPS address directly in Safari. Do not test inside a chat preview or embedded iframe.
5. Your phone's localhost refers to the phone, not your Windows PC. An ordinary HTTP link to the PC's LAN IP is not enough for camera/WebXR security requirements.

No Mac or native app build is required for these web AR implementations. Phone AR still depends on device and browser support.

## Assets and libraries

Original PixelBot mascot: assets/pixelbot.glb. It is a block-style mint and purple robot, about 35 cm tall at its original scale. It is not an official game character. Original game imagery remains replaceable illustrated placeholders.

The relevant AR libraries are bundled in vendor/ with licenses; see THIRD-PARTY-NOTICES.md. Most core files load locally, although native AR services may need internet.

## Shared PixelPedia screens

Home, Explore/search, game details, Saved, About and the demo contact form are retained. Saved games use browser-local storage. The contact form does not send or store messages. Each version starts on its AR page.

## Verification limits

Source JavaScript syntax and local assets checked. The test browser disables WebGL, so it could not render the model or verify camera tracking. Physical marker tracking, iPhone Quick Look and real room placement require testing on a compatible phone; they are not claimed as device-verified.
