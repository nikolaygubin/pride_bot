PGDMP     *    6                {         	   pridebase    15.4 (Debian 15.4-1.pgdg120+1)    15.4 (Debian 15.4-1.pgdg120+1)     )           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            *           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            +           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            ,           1262    16384 	   pridebase    DATABASE     t   CREATE DATABASE pridebase WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'en_US.utf8';
    DROP DATABASE pridebase;
                postgres    false            �            1259    16446 
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
       public         heap    postgres    false            %          0    16446 
   demo_users 
   TABLE DATA           -   COPY public.demo_users (user_id) FROM stdin;
    public          postgres    false    217            #          0    16436    promo 
   TABLE DATA           I   COPY public.promo (code, amount, count, active_id, date_out) FROM stdin;
    public          postgres    false    215            &          0    16450    refs 
   TABLE DATA           3   COPY public.refs (refcode, id, number) FROM stdin;
    public          postgres    false    218            $          0    16443 
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
       public            postgres    false    218            �           2606    16435    users users_pkey 
   CONSTRAINT     N   ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);
 :   ALTER TABLE ONLY public.users DROP CONSTRAINT users_pkey;
       public            postgres    false    214            %   u   x�Վ����^��:Τ���q�F,i��,'��=��Mi�P;��9����V.�#��s�S�I�<�����uȘH�X��슘R��4�m�9�am�/k����>3{j�B�      #   �   x�5�;�0Dk�,6گw�D�R*nqw�Ht�y3z�}Y��L�4m�D@R�U��>������A���؍H͋*6�V�1ht�d��cUG��U܃�ᘹ6�Kl������z(��68��K!flB�B�rE���s�9� l�'�      &   �   x�m��JAD�ٯ��_,�DaÞ���1M�LC�88����n�x}TWU׳��#G쐡������8R`Y+ŉ�V����s�	C����R�8��S=�Q��`(���?��#���T���6�E���l��ۋbC�\��kH�@Q�w�Sw皲��A!��c�<�}ȩ�Ȓ퟈i+qhʫ���rc���ߴ1%!�L_n������      $      x��01�4���4����� ��      "      x��[�r�ؕ��~
Ώ�J�H6� S�5�6��������X�"�&�$(���l��qǎ;�I�Ӊ�$5ˏ�вؑ�P�@�Ia�9�7���{�B �|�;�9� ���)
y�
K/�ʅJ��3�rMO�E��{�}�mw_{�_w;ݳn�{��t/�����h{1M;�д̈́�����ШL�.�I�������_�,h�����\z�\/-hJRӢ��Yմ�iM��h�r�[Ӛ���K���{�}ٽ�=��.}��7��%� ~{GNpr��8�Y�~�&ۂ�n`�s��'_�T���F�Z��L��TJ�;ʞ3�o�^5od?XNf��d����&m�}������w
Kpᅛ_��n��+�,B��{����z�f.W��sz���|�w�/�������0Q�\���}�;�/�+��}���N��¿zaX8���hy�^>�}�w��z% ��H8쁥��)7p��n����f�{�Ź�����0��xL���{c�/�y��>�˿����Z�����ķ��x;OD�C��<�Wҍ"�+Ll�R�y>�����'#�,J��L�a���Yh�eX����$����F�?�^�����������z��_��G1�T8���ۚ�m�ϥ�l!������ʮ3�ښ6c�n��{��	�����p&�� �]���pY��\/��f�@y�����S/.^�\������*Ι��S0�9�f;C_��U� 6�a����ƿ��_wo�`�L��!�zO=�(j�Ԩ�'F"!�[�&�B�0 _��/��ާ03ā�A��ٶq��Z�p�
���"L�uO�#���_$��
J��*�B�R}�"�UEP�"Fd1"�a�IT��pD��*I
|հ"
a8�5���r
�	�
��TZ7�t��/��LXD�
���촔0���dYaz7]?2�j��QI]�� }5���1-K$����Jz�?��gd��|YL�Rԛ��z� ���~�!���IR@� �8k�-ڗ�t���~f���8\ (.d���`���W�����!�BD	�� ,܇��i��_#�s}"�H�.��"�(6�I��F�����L"�`$n�^`K��R0A�q�� �y��l4�lT���J��7�63RMӏ�.u�K9*�c��Vʜ��4*�[1@Z/�K��VS��sբn��mp`rΏ�ޗ@�%����D���m�'7!��G�1F甸s
9���q��Α��g�����m�O��SB���bR�U�i�{��{��z }8�q8Q�TI��n6u�iB�H���&��z|��޷gD�z��g����^R����VS��m�s��v��H-/��������rC�r�p�$�;�R�����Z�|��H����PS y^���{�)��!P����4r��9��Oh��<rv���pW|	"g�b|�O�Z_pȐ-mSN�gsG#�.�D	)@D(�
�rA�O�.�p]3@���TU�rŜ��čK�B��ąkp��R���f�v��c��Z�~�V�R��,�$�bi͟�m����J�^i�{"�3:�!�Q�=�?�P&!�E��z�r�^�5&l��s��-�l���.���c�.�h�	�	z=�L��TdȢ�3�=��ҽ�}^B9i�<�<��<{��<�*�ՂY��.���>I9l��K�X�H(�����\��= �Y���Ꙃ�P-cV�93���{�*��i�5��3`62+�0�!����i$9����\K-�6��b&󥅴φ���,�6��|h:�Q*++��UԆf��B��#<�=A�a�1�c
 �%�sF� "��S�B_�^^A�`h<�3�ra@�&�l=~�z�!7�8J���~�V̔g�L�� d#R���I2v���sEЌfV�g�I����G��D#Øo)Ӟ#�=SZ1w4��UU�(�A��w���$��A8�'�n,���lr-b��xM0�oƕ�NT�����;����Hx:��t�J%A�|�*�f"���JtMٙ�H+�iG��y�?�4�3�Z3��q�%du��|,["�C�!F[ĒmB'�����iSx~#~I��*ӖX׿`!¯tW����q����L��$�u@;͇�HX�d�P�AH��ύMg,�sQ�R�P ���{d�V���HT�
�]��c=	���5�P}�v\�/<w����� �T��C�ܱ��oP���hiG�����Էs3�;YsaQ+nf�g�[;�.��.ǡ�A��%EJ�(��r�n�/��'���֘�Gt���5�%���A������m��d5�C;+C�I(s��e� �l���$4�%B�\��%o6o�'l��Ix*t��Gt�J�v�Z��)���d��O���\�E^�J(w�?d�W��5��U���@�Zp�h!L� �r�Z�U�T̥a �wD��sK�	[�������Q%e�2Bq��~���Ŗ�ޫ�WA��敵`S[+����[�&��� �j@/O��7.�cA�5X���
�'��P��1m�D�쌂8`�#����@]���@HO�>�#��Bͯ�$�=�fq0�ٛ� VU�Q �B5g�
�Q/T�j�0R� �a����f{��ʉ��,ԙ�J)!�	f�oU�Rr��.��f��И��ǐL'��Q��~3����ͅ��ԙ<2�!Q���eb��h�*���O�<}��V�������ѯ��3��A�3o`���-*��ڜ�PC,5v
-����3N�,���t�W��C���E/Y� >~N��c��C�F��-L�&d�K�������ˇ�
;��,"�{���^����9��
nY9S�)�C�N��t�X�W��v�Q�� �?a7�x19�\n&vW猍�j��������췲��Q�Ԛ��i����FVT�"����թ�����)}`�'W�R��!��(��"8��ȃ����Ν|$�`J�]���Z���o���T%T�2S�KzF���"|AU�15��aC��cU�v
1_���㙆6�2���5m�:�EEk+���Յ����qP�Ӵ\/��fx���7V?�Z�?�K���װ����b�y�_99(���\wb!gb���<(�IO ����d���ߐ��vb\��>��v�����|a$����/(A[��R�R�1"����L%�5��F8�E��g�*�2���f����ͦa�/$WWc)�<!Qi�*h}K_�+R���
��Z�lV��n���zqev�Xޜ/�������;L�aB ap��X}��D/Տo�C_��C6՜�$��Mh�Sr���p��m�4't�5�L�Q%��������fZ	�?�V�̚Q����񻅃��P��?�����4R՚���H�����n<�V*������J35}����o���[Q����/jڢu��k�����-);}(�ߪ&�&j�s�15c^�@L󒂸b%�����A��Eq�6f������p��	�/�W�fH��/ω����KB;%v��\�z�K�\��+o�
r�v��^ͮ����Ptr�U\am{�)�q���F���+ �įw�w=����;�^)��L^�X��n��w��]W�^���E�	�9g7�����Ք8�dK�CF����n�k\�i�	�b��3��|��Wn��p�	Dչm;!�ߋ5"�����[����Y��㉩f���Y��s��1��q}��vd�x�����8��e���YS����8Z�>���x�U0�+�l�=��0g9k��c��J!�L�Ind��+�L�p��37
y�]����'���E�3@4ꏫ�{��;R�:��ӥ���?_���g��E����c�sF,�x�.Z������j�@��\�R��Jδ'�n�fW��m�;�vM�U�}0�/$�W���O�����3Ļ����Α��
�f0.��8)1�^�N�w*s9��ػ#��J�*+S��|�m4��q�{\���No��}�PG�B��f�Y��k� G���RQ���7gT��X��%k� d  �5?���#6�V9[��j�����>��q)d�R�	�Ȣ?3����z '`��ya�73�ɇY�����-���_��ih��N�~��&����W���0�T1�0�&���ݏ ђ�w�+��60+���v�~������~w�ӗ�H��`�AR�� �V�u�������r�����tM���Ly$�Z�3���n�/��Mc%�~�,�����ݣ�9cZl�n�R~nI\h�k#X��<i�]oF�ݑ.F׌�[�֡H�W�����-�������Ե�&����L��>��N�~���ͷٮ	����W� �S�
W�q{��}��6$[��<yn���k�玏�E���C�����x����D�m�|��%oX�C���iU���(���h����C�Nj��(�i�3F-@�9덢5fu����!q|o��3jz��
U:��k��4#6{�.��i�s�nF���_�dY"<�,��m�8�C-NH}�1���4�nj�cLx1�t�^:�ԇ/�9#������oR{[rO��]�gR�y]��.*���W�p�ǺŖ���ݤ�؜.B�b�]<e�@���-�,{��օhz(Q}�����8}��|3�ʸ�1�1��lC�cF���
#h�mX���4F����M��^�[0_�2���ӊ�����N�ͽ��s���>��>x����g_�j1,���2@�o���ja��V8�g��U���3�r9���&-��|��~o���osq�����X�T��N������= ��"K1~�7�'ڏl[��U�)��'�*��RF�4�EÃ���[�g�,;a�=;,�p8�]�/��d�ִ�z6�Ҙ�7��c,���)�\_6̭X���7\"�>Y���������R������n`�|��8ȺM����9�e����I��F��1����L��:��3�q�z� W3�j>g�㶋FrQG}y���r���:*,�?0��"���j�`����D��U����E!ی��Ŏ�̹T�|�O��Jl������F9U]?���*�ٳ��x~�}F_|�Xr`w�p��^�����v�Z7�r���$����ɵ
N�O�:v��gj�^�B*n�Z�4��p�J{v!�kTżٯ5��+Qe�:�D����R!�p�L�A��Du�\I��s�����j<�F��w~�kx�w7��'Uc'�t_H�%dmfE*�z�B������n���J�?�gkеѾF'1>��d����뽞~on�0N����Le�\���Hd�{��Tog�"v�%�X<�����h��utp���c�5M[��ٹtь$6d��P>�����Pğ��B�>��t�'����;�<Ӱp�o���h ��H�R�^6jM3�iv�C���i����^��4R蟺�8������S�A���������$�<����� �g������a�h�B�,�Ĉ���>#�[�2����Yj�q�UֲO�LYE�)U�r5��~A�*'<! |E�)�J�Cl̮F
ٕ�����^=W�.��K��p�V<xU�{Ŝ���b�4Z�I�� �48�ɠ~�������wf%�X�%�	����^����� F��[b���q������b��GǱ"�����ߘ.�3>x����/�-{a��rRwɄ��{��e�pRy�3,��J�6�	����6By�5-ޥ<PDJ�zO�h�,�@`��`�/�����;�G��!���>��}�{�*f�[�S,� �~��uG�b��G��`Z��+�Y�L�G{�x�FD�oc7^?��Fe�v�X{�m���N.� �~�%���f��h�u���w�8}׋H��2��_y��?�}��،��V��p�[+���K�c��v�1'�1}��~�ȃ��n�Cե�k_p������wI�aߗ\.�EYQ䈬��Zƾ���F�O�L��Xx�s�Qy���{Q�ph�������$W��ي�ݛCw���9k9!J�����&=�{�3d��=�7%dW$�Vʧ^j�~E������̄w�n� �����g��JU�1�iP[�Ӻ�']x�]�1����;��x�t�/:�P��)0Q������;�3ϐB���w�g���<"�>T8p��.<���{�C�e     