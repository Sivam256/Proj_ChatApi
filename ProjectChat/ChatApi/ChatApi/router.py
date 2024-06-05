from Api.viewsets import ChatViewsets,MessageViewsets
from rest_framework import routers

router = routers.DefaultRouter()
router.register('chat',ChatViewsets)
router.register('message',MessageViewsets)