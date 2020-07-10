.. nuxt.jsとdjangoによるSSRアプリサンプル実装 documentation master file, created by
   sphinx-quickstart on Wed Jul  8 12:06:42 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

nuxt.jsとdjangoによるSSR - API アプリ実装サンプル
======================================================================

サーバ-クライアント通信
----------------------------------------------------------------------

SSR導入前
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. seqdiag::
   :desctable:

    seqdiag {
        browser  -> webserver [label = "GET /index.html"];
        browser <-- webserver;
        browser  -> webserver [label = "POST /blog/comment"];
        browser <-- webserver;
    }


SSR導入後
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. seqdiag::
   :desctable:

    seqdiag {
        browser  -> BFF  [label = "GET /", leftnote = "SSR例"];
            BFF -> apiserver [label = "GET /api/articles"];
            BFF <-- apiserver
            BFF -> apiserver [label = "GET /api/notices"];
            BFF <-- apiserver
        browser <-- BFF;

        browser  -> BFF  [label = "GET /articles", leftnote = "CSR例"];
        browser <-- BFF;
        browser -> apiserver [label = "GET /api/articles"];
        browser <-- apiserver

        browser  -> BFF  [label = "GET /hoge", leftnote = "CSR例:BFFにAPI提供機能を設ける"];
        browser <-- BFF;
        browser -> BFF [label = "GET /api/hoge"];
            BFF -> apiserver [label = "GET /api/foo"];
            BFF <-- apiserver
            BFF -> apiserver [label = "GET /api/baa"];
            BFF <-- apiserver
        browser <-- BFF;
    }


APIサーバにおける認証について
----------------------------------------------------------------------

- HTTPサーバ自体は、ステートレスなサーバ

  ステートレスということは、リクエストごとに関連性がないことをいう

- とはいえ、ログイン情報/画面間でのデータの引継ぎが必要な場合がある

  - そのために、セッションやクッキーを駆使して、ステートフルなやりとりをおこなっている

    - セッション : サーバー側に一時的にデータを保存する仕組み

- APIサーバの場合、どうすべきか

   - ログイン時に

   - ステートレスな状態を保ち、APIリクエスト間で状態管理すべきでない



サンプルソース
----------------------------------------------------------------------

- https://github.com/MasaruFukazawa/ssr_app


ライブラリ
----------------------------------------------------------------------

バックエンド
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Django

- Python webフレームワーク

- https://docs.djangoproject.com/ja/3.0/


Django REST framework

- Django でREST APIを作るためのモジュール

- https://www.django-rest-framework.org/

Django REST framework simplejwt

- JSON Web Token 型のトークンを扱うためのモジュール

- https://django-rest-framework-simplejwt.readthedocs.io/en/latest/index.html

djoser

- ユーザ登録/ログイン/ログアウト/パスワードリセットなどユーザ操作に関する機能を提供するモジュール

- https://djoser.readthedocs.io/en/latest/index.html


フロントエンド
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

nuxt.js

- Vue.js フレームワーク

- https://ja.nuxtjs.org/

axios

- BFF / ブラウザ で併用できるHTTPクライアント

- https://github.com/axios/axios
  
Auth Module

- nuxt.js用の認証モジュール

- https://auth.nuxtjs.org/api/auth.html#loggedin

cookie universal nuxt

- cookie universal の nuxt拡張

- BFF / ブラウザ で併用できるcookieモジュール

- https://github.com/microcipcip/cookie-universal/tree/master/packages/cookie-universal-nuxt


参考URL
----------------------------------------------------------------------

How To Build a Universal Application with Nuxt.js and Django

- https://www.digitalocean.com/community/tutorials/how-to-build-a-universal-application-with-nuxt-js-and-django


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
