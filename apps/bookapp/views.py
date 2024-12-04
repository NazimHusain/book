
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from apps.bookapp import models as BookModels
from .serializers import BooksSerializer
from django.db.models import Q
from apps.config.pagination import ApiPaginator

pagination_class = ApiPaginator()

class BooksListView(APIView):
    permission_classes = ()
    authentication_classes = ()
    

    def get(self, request, version):
        query_params = request.query_params
        filters = Q()

        if 'gutenberg_id' in query_params:
            filters &= Q(gutenberg_id=query_params['gutenberg_id'])
            
        if 'language' in query_params:
            filters &= Q(booksbooklanguages__language__code__icontains=query_params['language'])

        if 'topic' in query_params:
            topic = query_params['topic']
            filters &= Q(
                booksbooksubjects__subject__name__icontains=topic
            ) | Q(booksbookbookshelves__bookshelf__name__icontains=topic)
    
        if 'mime_type' in query_params:
            filters &= Q(booksformat__mime_type__icontains=query_params['mime_type'])

        books = BookModels.BooksBook.objects.filter(filters).distinct().order_by('-download_count')

        result_page = pagination_class.paginate_queryset(books, request)
        serialized = BooksSerializer(
            result_page, many=True, context={"request": request}
        )
        return pagination_class.get_paginated_response(serialized.data)


    







