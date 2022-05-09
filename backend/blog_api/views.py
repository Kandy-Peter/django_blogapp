from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer


class PostList(generics.ListCreateAPIView):
  queryset = Post.postobjects.all()
  
  #for checking the format data(JSON/XML) to be displayed
  serializer_class = PostSerializer

class PostDetail(generics.RetrieveDestroyAPIView):
  queryset = Post.objects.all()
  serializer_class = PostSerializer