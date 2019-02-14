#!/usr/bin/env python3
import psycopg2
import sys


class LogsAnalysis:
    try:
        conn = psycopg2.connect("dbname=news")
    except psycopg2.Error as e:
        print("Unable to connect to the database")
        print(e.pgerror)
        print(e.diag.message_detail)
        sys.exit(1)

    def MostReadArticle(self):

        cur = self.conn.cursor()
        sql = """select a.title, count(l.path) as cnt
                 from log as l join articles as a
                 on l.path like CONCAT('%', a.slug ,'%')
                 where path like '%/article/%' and status = '200 OK'
                 group by path, a.title
                 order by cnt desc
                 limit 3;"""
        cur.execute(sql)
        listOfArticles = cur.fetchall()
        cnt = 0
        for article in listOfArticles:
            cnt += 1
            print('''{} . {} - {} views '''.
                  format(cnt, str(article[0]), article[1]))

    def MostPopularArticleAuthors(self):
        cur = self.conn.cursor()
        sql = """select auth.name, count(auth.name) as CountOfTitlesPerAuthor
                 from log as l join articles as a
                 on l.path like CONCAT('%', a.slug ,'%')
                 join authors as auth
                 on a.author = auth.id
                 where l.path like '%/article/%' and status = '200 OK'
                 group by auth.name
                 order by CountOfTitlesPerAuthor desc
                 limit 3;"""

        cur.execute(sql)
        listOfAuthors = cur.fetchall()
        cnt = 0
        for author in listOfAuthors:
            cnt += 1
            print('''{} . "{}" - {} views '''.
                  format(cnt, str(author[0]), author[1]))

    def DaysThatLeadToError(self):
        cur = self.conn.cursor()

        sql = """select Date(time) as Date, count(*)
                 FILTER(WHERE status='404 NOT FOUND') * 100 /
                 count(*)::FLOAT  as percentage
                 from log
                 group by Date(time)
                 HAVING (count(*) FILTER(WHERE status='404 NOT FOUND') * 100 /
                 count(*)) > 1;"""
        cur.execute(sql)
        listOfDays = cur.fetchall()
        cnt = 0
        for day in listOfDays:
            cnt += 1
            print('''\n{} . "{}" - {:.2f} % errors for the day '''
                  .format(cnt, str(day[0]), day[1]))


if __name__ == '__main__':
    while(1):
        text = input("""
        What do you want to do?

            1. Get top 3 Most Read Article
            2. Get Authors popular articles
            3. Days that lead to error
            4. Exit

        Pick a number and press enter: """)
        choice = int(text)
        logsAnal = LogsAnalysis()
        if choice == 1:
            logsAnal.MostReadArticle()
        elif choice == 2:
            logsAnal.MostPopularArticleAuthors()
        elif choice == 3:
            logsAnal.DaysThatLeadToError()
        elif choice == 4:
            break

    logsAnal.conn.close()
