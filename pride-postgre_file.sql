PGDMP     "    ,    
            {            pride_postgre    15.3 (Debian 15.3-1.pgdg110+1)    15.3 (Debian 15.3-1.pgdg110+1)                0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false                       1262    16384    pride_postgre    DATABASE     x   CREATE DATABASE pride_postgre WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'en_US.utf8';
    DROP DATABASE pride_postgre;
                postgres    false            �            1259    16484 
   demo_users    TABLE     7   CREATE TABLE public.demo_users (
    user_id bigint
);
    DROP TABLE public.demo_users;
       public         heap    postgres    false            �            1259    16474    promo    TABLE     u   CREATE TABLE public.promo (
    code text NOT NULL,
    amount integer,
    count integer,
    active_id bigint[]
);
    DROP TABLE public.promo;
       public         heap    postgres    false            �            1259    16481 
   temp_users    TABLE     7   CREATE TABLE public.temp_users (
    user_id bigint
);
    DROP TABLE public.temp_users;
       public         heap    postgres    false            �            1259    16467    users    TABLE     �  CREATE TABLE public.users (
    id bigint NOT NULL,
    tg text,
    name text,
    photo text,
    town text,
    social_network text,
    work text,
    hooks text,
    expect text,
    online boolean,
    born_date text,
    purpose text,
    gender text,
    email text,
    is_sub_active boolean,
    date_out_active text,
    last_pairs bigint[],
    all_pairs bigint[],
    impress_of_meet integer[],
    active boolean
);
    DROP TABLE public.users;
       public         heap    postgres    false                      0    16484 
   demo_users 
   TABLE DATA           -   COPY public.demo_users (user_id) FROM stdin;
    public          postgres    false    217                      0    16474    promo 
   TABLE DATA           ?   COPY public.promo (code, amount, count, active_id) FROM stdin;
    public          postgres    false    215                      0    16481 
   temp_users 
   TABLE DATA           -   COPY public.temp_users (user_id) FROM stdin;
    public          postgres    false    216                      0    16467    users 
   TABLE DATA           �   COPY public.users (id, tg, name, photo, town, social_network, work, hooks, expect, online, born_date, purpose, gender, email, is_sub_active, date_out_active, last_pairs, all_pairs, impress_of_meet, active) FROM stdin;
    public          postgres    false    214            v           2606    16480    promo promo_pkey 
   CONSTRAINT     P   ALTER TABLE ONLY public.promo
    ADD CONSTRAINT promo_pkey PRIMARY KEY (code);
 :   ALTER TABLE ONLY public.promo DROP CONSTRAINT promo_pkey;
       public            postgres    false    215            t           2606    16473    users users_pkey 
   CONSTRAINT     N   ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);
 :   ALTER TABLE ONLY public.users DROP CONSTRAINT users_pkey;
       public            postgres    false    214                  x������ � �            x������ � �            x������ � �           x�-N�N�P<o�����4�\-&MM�1\Z�R��H�Uc"`�/�ă�А�M�|þ?�ALvw����UUU�U�`�un|�j���ЌM =<D�@LѰ��5����S3�U�^�)�I�h:�fܿ��]/��I�ԭ��Z�h��}������-)�v�{��0�.���Ν�ݺ~o?z�9(��%�gJ)���$�HEY.}Q�F�2��{�^E6�9w����/��i�u�5��,����}}�	-ؔ/9��f<��*<<�W$4%A� V��      