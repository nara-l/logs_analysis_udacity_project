#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import psycopg2

report_1 = 'Report #1:  What are the most popular three articles of all time?'
query_1 = """
select title, count(title) as page_views from articles join log
on concat('/article/', public.articles.slug) = public.log.path
where public.log.status like '%200%'
group by public.log.path, public.articles.title order by page_views
desc limit 3;
"""

report_2 = 'Report #2: Who are the most popular article authors of all time?'
query_2 = """
select public.authors.name, count(public.authors.name) as page_views
from public.articles join
public.authors on public.articles.author = public.authors.id join
public.log on concat('/article/', public.articles.slug) = public.log.path
where public.log.status like '%200%' group by public.authors.name order
by page_views desc
"""

report_3 = 'Report #3: On which days did more than 1% of requests lead to errors?'
query_3 = """
select * from (
    select total_errors.day,
    round(cast((100*total_404_errors.hits) as decimal) /
    cast(total_errors.hits as decimal), 2)
    as percent from
        (select date(time) as day, count(status) as hits from public.log group by day)
        as total_errors
        join
        (select date(time) as day, count(status) as hits from public.log where
        status
        like '%404%' group by day) as total_404_errors
    on total_errors.day = total_404_errors.day)
as p where percent > 1.0;
"""
