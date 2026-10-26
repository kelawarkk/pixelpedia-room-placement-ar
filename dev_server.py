"""Optional local server. Opening index.html directly also works."""
import argparse
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
import os

parser = argparse.ArgumentParser()
parser.add_argument('--host', default='127.0.0.1')
parser.add_argument('--port', type=int, default=5173)
args, _ = parser.parse_known_args()
SimpleHTTPRequestHandler.extensions_map.update({'.glb':'model/gltf-binary','.usdz':'model/vnd.usdz+zip','.js':'text/javascript'})
os.chdir(Path(__file__).resolve().parent)
ThreadingHTTPServer((args.host, args.port), SimpleHTTPRequestHandler).serve_forever()
