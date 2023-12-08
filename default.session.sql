-- DROP TABLE "alembic_version";

-- DROP TABLE "tokens";

-- DROP TABLE "users";
-- DROP TABLE "messages"
-- DROP TABLE "users"

-- UPDATE users SET is_superuser = True
-- WHERE users.id = 1;


INSERT INTO friends (user_id, friend_id, email)
VALUES (1, 2, 'friend@example.com');


INSERT INTO friends (user_id, friend_id, email)
VALUES (2, 1, 'friend@example.com');
