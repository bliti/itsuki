/* sqlite3 */

create table if not exists users (
  id integer primary key autoincrement,
  name varchar(255) not null,
  phone varchar(255) not null,
  email varchar(255) not null,
  organization varchar(255) not null,
  status varchar(255) not null,
  role varchar(255) not null
);