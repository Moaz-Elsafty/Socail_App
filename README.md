# Bookmarks

A small social app built with Django where people save images they find around the web, follow each other and see what their friends are bookmarking.

I built it to learn how the pieces of a real social site fit together: custom auth, social login, a follow system, an activity feed and some Redis on the side.

## What it does

- Sign up / log in with username or email, or with Google
- Bookmark images from any website using a browser bookmarklet
- Like images and follow other users
- Activity feed on the dashboard showing what the people you follow are doing
- View counter and a "most viewed" ranking, both stored in Redis
- Infinite scroll on the image list (plain `fetch`, no frameworks)

## Stack

Django 5 · SQLite · Redis · easy-thumbnails · social-auth-app-django · django-extensions · django-debug-toolbar

## Running it locally

You'll need Python 3.10+ and a Redis server running on `localhost:6379`.

```bash
git clone https://github.com/Moaz-Elsafty/Socail_App.git
cd Socail_App
python -m venv env
source env/bin/activate        # Windows: env\Scripts\activate
pip install -r requirements.txt
```

Create a `.env` file next to `manage.py`:

```
SECRET_KEY=your-secret-key
GOOGLE_OAUTH2_KEY=your-google-client-id
GOOGLE_OAUTH2_SECRET=your-google-client-secret
```

Then set up the database and start the server:

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

The app lives under `/account/`, so open http://127.0.0.1:8000/account/.

### Google login and the bookmarklet

Both expect the site to run on `mysite.com` over HTTPS. Point the domain at your machine by adding this line to your hosts file:

```
127.0.0.1 mysite.com
```

Then run the server with a local certificate:

```bash
python manage.py runserver_plus --cert-file cert.crt
```

and open https://mysite.com:8000/account/. Your browser will warn about the self-signed certificate the first time, which is expected.

To use the bookmarklet, drag the **Bookmark it** button from the dashboard to your bookmarks bar, then click it on any page with images.

## Project layout

```
account/   users, profiles, auth, follow system
images/    bookmarking, likes, views and ranking
actions/   activity stream
bookmarks/ project settings and urls
```
