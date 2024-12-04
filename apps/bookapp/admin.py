from django.contrib import admin
from apps.bookapp import models as booksModdels

class AdminBooksAuthor(admin.ModelAdmin):
    list_display = ("id","birth_year", "death_year","name",)

admin.site.register(booksModdels.BooksAuthor, AdminBooksAuthor)



class BooksBookAdmin(admin.ModelAdmin):
    list_display = ("id","download_count", "gutenberg_id","media_type","title")
admin.site.register(booksModdels.BooksBook, BooksBookAdmin)



class BooksBookAuthorsAdmin(admin.ModelAdmin):
    list_display = ("id","book", "author")
admin.site.register(booksModdels.BooksBookAuthors, BooksBookAuthorsAdmin)

    
class BooksBookBookshelvesAdmin(admin.ModelAdmin):
    list_display = ("id","book", "bookshelf")
admin.site.register(booksModdels.BooksBookBookshelves, BooksBookBookshelvesAdmin)

    

class BooksBookLanguagesAdmin(admin.ModelAdmin):
    list_display = ("id","book", "language")
admin.site.register(booksModdels.BooksBookLanguages, BooksBookLanguagesAdmin)

    

class BooksBookSubjectsAdmin(admin.ModelAdmin):
    list_display = ("id","book", "subject")
admin.site.register(booksModdels.BooksBookSubjects, BooksBookSubjectsAdmin)

class BooksBookshelfAdmin(admin.ModelAdmin):
    list_display = ("id","name")
admin.site.register(booksModdels.BooksBookshelf, BooksBookshelfAdmin)



class BooksFormatAdmin(admin.ModelAdmin):
    list_display = ("id","mime_type","url","book")
admin.site.register(booksModdels.BooksFormat, BooksFormatAdmin)


class BooksLanguageAdmin(admin.ModelAdmin):
    list_display = ("id","code")
admin.site.register(booksModdels.BooksLanguage, BooksLanguageAdmin)


class BooksSubjectAdmin(admin.ModelAdmin):
    list_display = ("id","name")
admin.site.register(booksModdels.BooksSubject, BooksSubjectAdmin)




