DROP TABLE IF EXISTS www_bet;
CREATE TABLE "www_bet" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "createdAt" datetime NULL, "finish" integer NOT NULL, "driver_id_id" bigint NOT NULL REFERENCES "www_driver" ("id") DEFERRABLE INITIALLY DEFERRED, "person_id_id" bigint NOT NULL REFERENCES "www_person" ("id") DEFERRABLE INITIALLY DEFERRED, "race_id_id" bigint NOT NULL REFERENCES "www_race" ("id") DEFERRABLE INITIALLY DEFERRED, "user_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED, "beer" bool NOT NULL, "updatedAt" datetime NULL);
INSERT INTO www_bet(id,createdAt,finish,driver_id_id,person_id_id,race_id_id,user_id,beer,updatedAt) VALUES('1','2023-03-06 16:20:34.130253','18','3','1','1','1','0','2023-03-06 16:16:13.156540'),('2','2023-03-06 16:21:22.781167','8','4','2','1','1','1','2023-03-06 16:21:22.781167'),('3','2023-03-06 16:30:32.484142','26','4','1','2','1','0','2023-03-06 16:24:19.401107'),('4','2023-03-06 16:47:47.721363','2','3','1','3','1','1','2023-03-06 16:24:42.096658'),('5','2023-03-06 16:47:03.432498','10','1','2','2','1','1','2023-03-06 16:39:20.580791'),('6','2023-03-06 16:42:01.686450','14','2','2','3','1','0','2023-03-06 16:39:46.822943'),('7','2023-03-13 08:59:10.164114','1','5','2','4','1','1','2023-03-13 08:59:30.106119'),('8','2023-03-13 08:59:55.271139','2','4','1','4','1','0','2023-03-13 08:59:55.271139');