from api.serializers import CommentSerializer, FollowSerializer
from api.serializers import GroupsSerializer, PostSerializer
from django.shortcuts import get_object_or_404
from posts.models import Follow, Group, Post
from rest_framework import filters, permissions, viewsets
from rest_framework.pagination import LimitOffsetPagination

from .permissions import OwnerOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (OwnerOrReadOnly,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupsSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        post = get_object_or_404(Group, post_id=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user, post=post)
        return post


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (OwnerOrReadOnly,)

    def get_queryset(self):
        return get_object_or_404(
            Post, pk=self.kwargs['post_id']
        ).comments.all()

    def perform_create(self, serializer):
        author = self.request.user
        post = get_object_or_404(Post, author=author)
        serializer.save(author=author, post=post)
        return post


class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        return Follow.objects.select_related(
            'following'
        ).filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
