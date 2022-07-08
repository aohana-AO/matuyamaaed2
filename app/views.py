from re import template

from django.http import request
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
import feedparser
import json
import pprint


class IndexView(TemplateView):
    template_name = 'app/index.html'


class AllhosView(TemplateView):
    template_name = 'app/allhospital.html'


class KyuuhosView(TemplateView):
    template_name = 'app/99hospital.html'


class BlogView(TemplateView):
    template_name = 'app/site.html'


class NewsView(View):
    def get(self, request, *args, **kwargs):
        # RSSのスクレイピング

        url = 'https://news.google.com/news/rss/search/section/q/AED/AED?ned=jp&amp;hl=ja&amp;gl=JP'

        d = feedparser.parse(url)
        news = list()

        for i, entry in enumerate(d.entries, 1):
            p = entry.published_parsed
            sortkey = "%04d%02d%02d%02d%02d%02d" % (p.tm_year, p.tm_mon, p.tm_mday, p.tm_hour, p.tm_min, p.tm_sec)
            sortkey2 = "%04d.%02d.%02d" % (p.tm_year, p.tm_mon, p.tm_mday)

            tmp = {
                "no": i,
                "title": entry.title,
                "link": entry.link,
                "published": entry.published,
                "sortkey": sortkey,
                "sortkey2": sortkey2
            }

            news.append(tmp)

        news = sorted(news, reverse=True, key=lambda x: x['sortkey'])

        pprint.pprint(news)
        return render(request, 'app/NewsView.html', {'news': news})

