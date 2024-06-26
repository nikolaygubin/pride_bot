PGDMP          6                {         	   pridebase    15.4 (Debian 15.4-1.pgdg120+1)    15.4 (Debian 15.4-1.pgdg120+1)     )           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            *           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            +           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            ,           1262    16384 	   pridebase    DATABASE     t   CREATE DATABASE pridebase WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'en_US.utf8';
    DROP DATABASE pridebase;
                postgres    false            �            1259    16462 
   demo_users    TABLE     7   CREATE TABLE public.demo_users (
    user_id bigint
);
    DROP TABLE public.demo_users;
       public         heap    postgres    false            �            1259    16436    promo    TABLE     �   CREATE TABLE public.promo (
    code text NOT NULL,
    amount integer,
    count integer,
    active_id bigint[],
    date_out text
);
    DROP TABLE public.promo;
       public         heap    postgres    false            �            1259    16450    refs    TABLE     ]   CREATE TABLE public.refs (
    refcode text NOT NULL,
    id bigint[],
    number integer
);
    DROP TABLE public.refs;
       public         heap    postgres    false            �            1259    16443 
   temp_users    TABLE     7   CREATE TABLE public.temp_users (
    user_id bigint
);
    DROP TABLE public.temp_users;
       public         heap    postgres    false            �            1259    16429    users    TABLE     �  CREATE TABLE public.users (
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
       public         heap    postgres    false            &          0    16462 
   demo_users 
   TABLE DATA           -   COPY public.demo_users (user_id) FROM stdin;
    public          postgres    false    218            #          0    16436    promo 
   TABLE DATA           I   COPY public.promo (code, amount, count, active_id, date_out) FROM stdin;
    public          postgres    false    215            %          0    16450    refs 
   TABLE DATA           3   COPY public.refs (refcode, id, number) FROM stdin;
    public          postgres    false    217            $          0    16443 
   temp_users 
   TABLE DATA           -   COPY public.temp_users (user_id) FROM stdin;
    public          postgres    false    216            "          0    16429    users 
   TABLE DATA           �   COPY public.users (id, tg, name, photo, town, social_network, work, hooks, expect, online, born_date, purpose, gender, email, is_sub_active, date_out_active, last_pairs, all_pairs, impress_of_meet, active) FROM stdin;
    public          postgres    false    214            �           2606    16442    promo promo_pkey 
   CONSTRAINT     P   ALTER TABLE ONLY public.promo
    ADD CONSTRAINT promo_pkey PRIMARY KEY (code);
 :   ALTER TABLE ONLY public.promo DROP CONSTRAINT promo_pkey;
       public            postgres    false    215            �           2606    16456    refs refs_pkey 
   CONSTRAINT     Q   ALTER TABLE ONLY public.refs
    ADD CONSTRAINT refs_pkey PRIMARY KEY (refcode);
 8   ALTER TABLE ONLY public.refs DROP CONSTRAINT refs_pkey;
       public            postgres    false    217            �           2606    16435    users users_pkey 
   CONSTRAINT     N   ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);
 :   ALTER TABLE ONLY public.users DROP CONSTRAINT users_pkey;
       public            postgres    false    214            &   *   x���  �?��#�.�?��mGN�aO���������      #   :   x���430�44յ�FF&�F�F\�!�~.�A!�ƨ�ƺ���FF\1z\\\ �P�      %   �   x�m�Ak�0��ɏkC��@]�BFN�h�X�ld�̌��9�M�1?==��AT���!�!�>/բ�(xK�6�
�H��vJ�[
�
B�2��P�1}�р�C�`�꺣�l#jA���G�Ѓ^�l�"KO��@.+v7��(�{02[{��X~���+%T��3O�F� ���H��lV�*�}�l��h�`�S�h��kV]w���G.�=����r�.��m���]]�_'8��      $      x��01�4���4����� ��      "      x��\�nٕ��~
Ώ�d��b��FQ2���4@ɒX�&7QA����N{ܙL��Ng�Y~"�R7��z�M�9��[��f���e-���S�|�;ۭ��pT�"�T��0�f�P�TM{�l��/���W݋�k��n�{�=�^�Ǜ�e�����}/��G���W������݅9���0���8�]_::8�ˬ��]I�z�PT���>7��]_���ƴ����f��v�ݗ�v��u�w��c�(|zg�p��8�Y�}�U70�9�������?��C�\�{�Q
e+��eϙ�k���r?_NeÉT����&m������hW�X��&��n����н��¢���S�6Ͳ�he_��p�;�%mw/�x7��]��_�N��K�t#u�/{_��¥>U�g?�zO`�S�/á�/q&߮OPB�O�j������&L�{�{���QV�P��{�W�(�/��06~�����n�n��;Ń��7���Z�t��(G�yj�dXE\Wl�R6}�����}����òo�N��=\U��B�њ���i-g(�ms�p'g/,�����Lxk�t�p:��b�ݰ()RjG��k�,�1���5�&`i&�ʕ����ؚ�3��VfҎ�h�O� k��$�����f�#~\�[x(B �'�����+\�����縰���)��3<���GaI���+��Gp���c�����pEA��E��K�� ��H�S6a�wzO�!��%i�����=����J�vp:p���{���O��?	�g>e؊ز��-��N������ �S��-=�|n��ڰ���O��Z���ˡr�0E`��c�*k�����j�(T�R���@hX��k? �i��G񺹼�Z�?���xV(�V֏��f|9	x�"^!�W��-}����[�W�̙�5d�'���� ���5h���8�}_ TnLs��в3j�q� ��w u�����@HO�=���j>Q	T�J�C� �i8;����&º�n��4���G�`p��YBk�F�EAUŨ�� wQ��V�`[u�Ղe�%A5���7ZR�s���/B�a���=H)�Ë�+���'l��`���Rsuuaw7�J��&8�����\&�����[YU�U7JZ�ͷBK�@0�rQ�h��2�sXF��	�3�?� W�n;����AZ��8~TB���F �	��)��K�qm1B,5V�S��wp���v�S�������QB�!��ˢ���+8����ظ\5�=��?0	9O�a���a5�&"���HT��0��+���|nZ_`>��Fr����m���Q�"�,F}S�X�W��v���� �?a7�x15�^n%wW笍�j�I���:�X6r��Q��[���{���WQQU��;'S�Dχ�n%�v�18NA|K��� ʼ|!��$�`�p'� �s'I�G2�RU�c�Ŵ%���F�R"aIR�Z��0���	��	���=�6L63�oT��ԁI��k�Y��ǋ��:����qcw+m��W�띜W�(�KF9�hټY-������C��{�3�ݷ�E�7�a<�&��Z
�}�0�\������>qu~��b�CV�V�c��Ԃ� ɾ_��*���j�7-,DeM�J������\ ����,��,hQ�7�3�a���Af���=A��_z|�^�3Neϊ%0��a2W�	�g�{)��c��[-]��!�өnכ������aZ[h�����F�d~��ό�I��2Y*1��!����=Dk���3&n`om��5������L����9��'$S�$��3�	����?Ը�ir=ҥ�ʩ�QΙG3��)"JQ�-@���M���2�^��/U��PA�{��A�{�7U5f�l�t�W�p�N1�Fz$�<��rG�d���-��Ə[���TAS��;U4 I���Z05���[ٝ�ֽ������e�`�_�T�`��;��ރ�t��C,�J`xM��{�q�*�N�Y�7B�Y��d��ސ�Q6Fs_Sl��$`>yy�[
#�ާ[Y-�uI�$�I�e@$E�"
���G#�@�@UQ-/�t60 �_D8Z}S��%`�j޴ӆ�ܠV~�k9�L�O��H�<B�d����z��,���˵y:�ة|i!c$rZ,�닻-�f.�Nn����vl5�����+~�g��/tX�ױ ���[ʹ���	��+G�~?%��Ox2G1#"�l���멏̘�(=�J!�����R	Q��#!Hϩ 񄕽�(�x�x����74!�Yo�,Z����1��\z���4�hd�!�aړ!���JD�M�E�h�(��}MNS��'ƅ9�=���˙��K�E-MJ���fB)�`�/ ����|~1�MG���NQ$�G�%�ld����0+~ʒ��Q֢2Й�?!��R)Oɪ�y�f��.���{�F|BN�,���������z�h�6�M:V�P"�m��M����"�F��*�5'N=Ã�~
�\����n��ޝ��<�|���%���F��t�cY��'m״����Q)�J4�b�P4JF@��4��/(�;%��2�MG��Rc���Z5a�4���o��3���QLll���zQ]h.����9]o���nis��n0��^�ExI�y�P#PW҆�3k��W.1R,0��'FÆ7
Խ�����Pэ������7�o��L�Cċp�g��x?��ϡ1$�
j�"�?��,I�w�x|L--���hX�M%�٬Y���t�ĳC�%[����\�"�{�Lq5_.�[;�V�.c��D�n���Ii�^���/���D�b�ʥ�X��7^�U��/�y -�1'�3^NyH���%���=!�NY��S�bm&j*�8!�C�P��᩻��`�N=*��$�z9g���q�0˕BH�N�jaP�ɢK:
�����}<�7�I$%��a�Q�+�����l�y���H��~Ψ���1���Lt1��J�z�Zɯ���%�y	yhkZl�n�R~nI\h��#0��?/h֛�J�y$~�<�0��r�Br`�K �|�6'S�Þz?Pk푙q�U@<�Cr.�ð~�w�הi3��-e�|�3'�+ϸ�_�~�Sd7-g�S�'z����)��ᚳ��!hd�1h��xH����ƚe߲��q;ı�i�O�*�p|!o�8:��#�����hD�g�&;Ay����fD�����=H7���R�n�f+I���`��6��)>EXN}�1�K^�� �;kd�U`FƏz��IF��A�܉q�c?����:��÷�̈����^]��E0�E�=��������y�r�����31kg��%��KQ����~�+����@O'O���|��օ��Lb�.C��y�8�܏�;���[/�'��M_8 f��O�8��hQ�ϤUAs�d(l=%�a�N��_���)8gS0[��̷	Њ����q��P��I�e��C�W����g���|�V��n ��C���-[]o �{Ə��V���T�e3[�	&-M�[>�u?n�v�ɮ�O2���)�`�c�'��'k��C,2������7BX.[��WW_)B+Q	{�l KY�*-_��<Wy���8%21���;˦�i��R~ie'�eM׳��Js.��g�1&׶�i�\_7��x���7�����k0yW�؟k.K����vs������ �9:���9��`O{R���H�v;�N�{���Q�=֌�q[F����V5o6�qm�� �-���V!wT�}�6(?B�Ж����]��)�8��ӥ���|0_�iǳ[�b��ņ�/c�5gœ����bcs���[�d����*�bOޱ56�%\��S��·����-#�x��t�:��0}f�x��Q���x��ke�=ȯ^����֙�FU����r�T�������կ+��]@��H���@��Sup���];��x5�Z�,��kB6����PM,,oΨJ��"i�� >  Jik~f�`	��!6�r>����J�Ņ�cc����J�&D"_�O<zy�܃���TD������_�����ñmE��e���n �C#����Θ�C?�B�!�y�7��G�};dB�U�k�b�6�+����Y�,��ъ|��\�;`��q�S�I����sN��2�r�`&�,L�G�o��%w-R��K��zu��y�(�Z�ս�і=�N��/���# arS]L���7�������Sr2'~�}F?�xj`3	8�;�a)?|T���B�\i������\�����(W��e��R�P/Ѱ���m��kUwX�wi���;9F"�����׌D��Jq{�^8P����DZH"��L96golN�&b1i�D�z'�ww8��ʗ"�~���F��E?�]Q� 2yꓻ#�(o�c܃��kP��h j����������N�Qw`�-��r��AŮ�ɕ�4miEh�?g��7��c�L8���qӮofģ�X"W�����{����.6+;����;R��N.Vae�,��1�Y^�+�mœNoӆ�D��\�����?�k;�=!�g���jy"촜Bn~Y*��V��N,ϟy8&4t6@sF���ⶇ䐯����q�<{o��ꙩ9�!֚OF�]�>��-��ΗEYQ䨬x����Jx�չ�75k�������chW�����a#(ݟu%��9�f+�~o�aVN6��IQ�]>0��7�.@�MƐ3B��o�WT�d�ا~����(nރ!݄~���c� ����z��R�lL��@�j���w�M�s�o�����6�0_wɪ;��+J:�$�RyY�������Nw E�&���f�j�e��.]����!����F�.��r���ci?VRua�1Jۉ`���i�$���Q�*����6�ǭ����+�r1WYX��V���_;�
�f�q_Br�/�Vr�ݧ� �ѧ��R�����7"ǻW����))>_��q�P,�^�N�X���7��|��G���.���
�����:̆9�K����(��ګ�I,<�H�aft��M%�5���l�~чy����܆Պ�7��aZ��-����Z]���
��+����[�Bc�jD��wB\�*�L�Ui�\nL�Wf�����℆�^� ���1��:ֹB~�:L}Gۡ-ۧԇ��*�B��,���?�=�N� �8���^<u�f��ޙ�J��E~�^�]���4[`�1���3�64�w�'��d[�jMT�P ���֤��a�ZJIyyM�fj�F};�����bBu!{_����1`*�J�~3lH��C��NI*�*��1I�'�5������O��b��z�
V�
q�8�_&q�?���.HBj5��
{�욍�@۽$�;��r���72o�G��yKu�KVA�-��~�Ҡ�Ptq�m����v ������F�v��uǾS ��s�����j6op,De�D=�DN�Q�wǟ�~��9�jL��ՆY�m�/h�#�����+{����z,ٜ]�r+	]7�Ž�Y�/�F���m�v+>�������)o���*�E�xsDN�͑A�'ǤϽ�5��z|v�?��Hl,�S���N�����u�G����u/��Ќ��ꃟ�bt��ۮa�M�:z�+_�?f������Kx�v���𤗁&���u,p:u��Wni�g
?�[m�H���m��v��czg2(��}[[Ѫ5�2 +��2��j�58קz����Bﵞ(��o*gADm8_�����8�l� @f�;-%�D~C�/4���dk���(:SO��k��$qv.S���Y88�*��+#n�O�2��0N���6�A�:N&U�l��ҿ����!t �C�
2J��݋!A��a=��F���3�����S�뜼�u�qz�l�������� �������_��{�py��{�qȨ�B�4�T*�n`�#�����f���������V�7��@&cV�e��5�aY��k2�f+��K�naz7S?��j��QI]�ŷ&���z.�L5�͕ݕ�Jp$pF8:ה*E�ګg�2Z؏qA�&��/��|5_8(�
"��Fρ��<���_�,��%����Tb Fb1�G�>��o(¡e     