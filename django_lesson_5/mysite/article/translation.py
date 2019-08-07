from .models import Article
from modeltranslation.translator import translator, TranslationOptions


class ArticleTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

translator.register(Article, ArticleTranslationOptions)
