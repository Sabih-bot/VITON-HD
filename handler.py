from runpod.serverless import handler
import base64
import os

@handler
def viton_test(job):
    return {
        "status": "VITON-HD endpoint live!",
        "output_img": "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAYEBQYFBAYGBQYHBwYIChAKCgkJChQODwwQFxQYGBcUFhYaHSUfGhsjHBYWICwgIyYnKSopGR8tMC0oMCUoKSj/2wBDAQcHBwoIChMKChMoGhYaKCgoKCgoKCgoKCgoKCgoKCgCcijrCfZBuqDzBWp3qSrBEZCqBUfQVz4CWGHWF91iaEw/wAARCAAIAAoDASIAAhEBAxEB/8QAFQABAQAAAAAAAAAAAAAAAAAAAAv/xAAhEAACAQMDBQAAAAAAAAAAAAABAgMABAUGIWGRkqGx0f/EABUBAQEAAAAAAAAAAAAAAAAAAAMF/8QAGhEAAgIDAAAAAAAAAAAAAAAAAAECEgMRkf/aAAwDAQACEQMRAD8AltVZ5b2iJ4S7bU7O7m9kD3V0H/2Q==",  # test image
        "delay_time": 2
    }
