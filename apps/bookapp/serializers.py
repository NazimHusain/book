from rest_framework import serializers
from .models import (
    BooksBook,
    BooksAuthor,
    BooksLanguage,
    BooksSubject,
    BooksBookshelf,
    BooksFormat,
)


class BooksFormatSerializer(serializers.ModelSerializer):
    class Meta:
        model = BooksFormat
        fields = ['id','mime_type', 'url']


class BooksAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = BooksAuthor
        fields = ['name', 'birth_year', 'death_year']


class BooksSerializer(serializers.ModelSerializer):
    authors = serializers.SerializerMethodField()
    languages = serializers.SerializerMethodField()
    subjects = serializers.SerializerMethodField()
    bookshelves = serializers.SerializerMethodField()
    formats = serializers.SerializerMethodField()

    class Meta:
        model = BooksBook
        fields = ['id','title', 'authors', 'languages', 'subjects', 'bookshelves', 'formats',"gutenberg_id"]

    def get_authors(self, obj):
        authors = BooksAuthor.objects.filter(booksbookauthors__book=obj)
        return BooksAuthorSerializer(authors, many=True).data
        

    def get_languages(self, obj):
        return BooksLanguage.objects.filter(booksbooklanguages__book=obj).values('code')

    def get_subjects(self, obj):
        return BooksSubject.objects.filter(booksbooksubjects__book=obj).values('id','name')

    def get_bookshelves(self, obj):
        return BooksBookshelf.objects.filter(booksbookbookshelves__book=obj).values('id','name')

    def get_formats(self, obj):
        return BooksFormatSerializer(
            BooksFormat.objects.filter(book=obj), many=True
        ).data
