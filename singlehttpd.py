# Based on the example at:
# https://aiohttp.readthedocs.io/en/stable/web_lowlevel.html#run-a-basic-low-level-server
import os
import asyncio
import argparse
import functools
from aiohttp import web


parser = argparse.ArgumentParser()
parser.add_argument('-l', '--listen-host', default='0.0.0.0')
parser.add_argument('-p', '--listen-port', default=8080, type=int)
parser.add_argument('path')


async def handler(args, request):
    filename = os.path.basename(args.path)
    headers = {'Content-Disposition': 'attachment; filename=' + filename}
    return web.FileResponse(args.path, headers=headers)


async def run_server(loop, args):
    server = web.Server(functools.partial(handler, args))
    await loop.create_server(server, args.listen_host, args.listen_port)
    print("======= Serving on http://%s:%s/ ======" %
          (args.listen_host, args.listen_port))
    while True:
        await asyncio.sleep(100*3600)


def main():
    args = parser.parse_args()
    loop = asyncio.get_event_loop()

    try:
        loop.run_until_complete(run_server(loop, args))
    except KeyboardInterrupt:
        pass
    loop.close()


if __name__ == '__main__':
    main()
