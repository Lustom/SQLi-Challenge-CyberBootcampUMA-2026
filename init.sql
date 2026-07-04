CREATE TABLE datos_publicos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario TEXT,
    role_usuario TEXT,
    email TEXT
);

CREATE TABLE ctf_admin_secret_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre_clave TEXT,
    valor TEXT
);

INSERT INTO datos_publicos (usuario, role_usuario, email) VALUES ('j.perez', 'Operario', 'jperez@logistica.com');
INSERT INTO datos_publicos (usuario, role_usuario, email) VALUES ('a.gomez', 'Supervisor', 'agomez@logistica.com');
INSERT INTO datos_publicos (usuario, role_usuario, email) VALUES ('m.lopez', 'Conductor', 'mlopez@logistica.com');
INSERT INTO datos_publicos (usuario, role_usuario, email) VALUES ('ctf_master', 'Admin', 'admin@logistica.com');

INSERT INTO ctf_admin_secret_data (nombre_clave, valor) VALUES ('API_KEY_EXTERNA', 'AK-998123-X');
INSERT INTO ctf_admin_secret_data (nombre_clave, valor) VALUES ('FLAG_ACCESO', 'flag{un10n_3num3r4t10n_m4st3r}');