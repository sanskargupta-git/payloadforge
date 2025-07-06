import argparse
import base64
import urllib.parse
import html

def base64_encode(data):
    return base64.b64encode(data.encode()).decode()

def base64_decode(data):
    return base64.b64decode(data.encode()).decode()

def url_encode(data):
    return urllib.parse.quote(data)

def url_decode(data):
    return urllib.parse.unquote(data)

def html_encode(data):
    return html.escape(data)

def html_decode(data):
    return html.unescape(data)

def main():
    parser = argparse.ArgumentParser(description="🛠️ PayloadForge – Encoder/Decoder Toolkit")
    parser.add_argument("-m", "--mode", required=True, choices=["b64e", "b64d", "urle", "urld", "htmle", "htmld"], help="Encoding/Decoding mode")
    parser.add_argument("-d", "--data", required=True, help="Data to encode/decode")
    args = parser.parse_args()

    try:
        if args.mode == "b64e":
            print(base64_encode(args.data))
        elif args.mode == "b64d":
            print(base64_decode(args.data))
        elif args.mode == "urle":
            print(url_encode(args.data))
        elif args.mode == "urld":
            print(url_decode(args.data))
        elif args.mode == "htmle":
            print(html_encode(args.data))
        elif args.mode == "htmld":
            print(html_decode(args.data))
    except Exception as e:
        print("❌ Error:", str(e))

if __name__ == "__main__":
    main()
