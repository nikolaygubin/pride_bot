PGDMP                         {            pride_postgre    15.3 (Debian 15.3-1.pgdg110+1)    15.3 (Debian 15.3-1.pgdg110+1)                0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false                       1262    16384    pride_postgre    DATABASE     x   CREATE DATABASE pride_postgre WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'en_US.utf8';
    DROP DATABASE pride_postgre;
                postgres    false            �            1259    16820 
   demo_users    TABLE     @   CREATE TABLE public.demo_users (
    user_id bigint NOT NULL
);
    DROP TABLE public.demo_users;
       public         heap    postgres    false            �            1259    16823    promo    TABLE     u   CREATE TABLE public.promo (
    code text NOT NULL,
    amount integer,
    count integer,
    active_id bigint[]
);
    DROP TABLE public.promo;
       public         heap    postgres    false            �            1259    16828 
   temp_users    TABLE     7   CREATE TABLE public.temp_users (
    user_id bigint
);
    DROP TABLE public.temp_users;
       public         heap    postgres    false            �            1259    16831    users    TABLE     �  CREATE TABLE public.users (
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
       public         heap    postgres    false                      0    16820 
   demo_users 
   TABLE DATA           -   COPY public.demo_users (user_id) FROM stdin;
    public          postgres    false    214                      0    16823    promo 
   TABLE DATA           ?   COPY public.promo (code, amount, count, active_id) FROM stdin;
    public          postgres    false    215            	          0    16828 
   temp_users 
   TABLE DATA           -   COPY public.temp_users (user_id) FROM stdin;
    public          postgres    false    216            
          0    16831    users 
   TABLE DATA           �   COPY public.users (id, tg, name, photo, town, social_network, work, hooks, expect, online, born_date, purpose, gender, email, is_sub_active, date_out_active, last_pairs, all_pairs, impress_of_meet, active) FROM stdin;
    public          postgres    false    217            t           2606    16841    demo_users demo_users_pkey 
   CONSTRAINT     ]   ALTER TABLE ONLY public.demo_users
    ADD CONSTRAINT demo_users_pkey PRIMARY KEY (user_id);
 D   ALTER TABLE ONLY public.demo_users DROP CONSTRAINT demo_users_pkey;
       public            postgres    false    214            v           2606    16837    promo promo_pkey 
   CONSTRAINT     P   ALTER TABLE ONLY public.promo
    ADD CONSTRAINT promo_pkey PRIMARY KEY (code);
 :   ALTER TABLE ONLY public.promo DROP CONSTRAINT promo_pkey;
       public            postgres    false    215            x           2606    16839    users users_pkey 
   CONSTRAINT     N   ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);
 :   ALTER TABLE ONLY public.users DROP CONSTRAINT users_pkey;
       public            postgres    false    217                  x������ � �            x������ � �      	      x�3505�21z\\\ �S      
   {  x���]O�Pǯ��7���@��ʃ-���"˒�D@���۲|�[$aK�]mɖ}4��}��|�=�.�0n����y^����@ (eP$�{���c�$U$�LWh9Ai��4������F4�M#�K]��êȅ�AJS�NU5�����k�n3�n���
�Q
-�<ke��s�5�ȶm�7�.-5k|��]��×��I6H�D��~�n����\��1����>^�x� H>��wv���K�cC\OaS���p��[{���	3��70b'>�#�r}g�Y��䖼���	>��z}?m��C%Y&˦Q����66�V������+9�����HT�I��Z�ն���B�����Z�]��I�bB[k��V�L{��g�y}���ݮ�ͫH���
���
��'���'e�ـc}��X�|���+,=G?��k�A��Ƌ��sE)�Ő/H�5k�ЋF�@/Zf�"�K�r�q�N��|@3����i�Fj3k��f%���5�@��E�1+��֫��ͦ]R�4�c�������Sv�G��2��{"
`�<�Y������;���I];��8t�7F�cWyxXL��;us�s4O1&���eo���a�<s�w�Q�/x�������     