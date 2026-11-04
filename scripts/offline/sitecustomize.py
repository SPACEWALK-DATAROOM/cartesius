"""Offline harness: user explicitly excludes external API/network execution."""
import sys

def _offline(event,args):
    if event in ('socket.connect','socket.getaddrinfo'):
        raise RuntimeError('Offline test harness forbids network access: '+event)
sys.addaudithook(_offline)
