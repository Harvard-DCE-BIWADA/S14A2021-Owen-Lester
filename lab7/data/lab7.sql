DROP TABLE IF EXISTS users CASCADE;
CREATE TABLE users (
    uid serial NOT NULL PRIMARY KEY,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    date_registered TIMESTAMP NOT NULL DEFAULT NOW()
);

INSERT INTO users (username, password) VALUES ('test_user1', 'test_pw1');
INSERT INTO users (username, password) VALUES ('test_user2', 'test_pw2');
INSERT INTO users (username, password) VALUES ('e14a', '123');

DROP TABLE IF EXISTS posts;
CREATE TABLE posts (
    pid serial NOT NULL PRIMARY KEY,
    uid serial NOT NULL,
    content TEXT NOT NULL,
    date_created TIMESTAMP NOT NULL DEFAULT NOW(),
    FOREIGN KEY (uid) REFERENCES users(uid)
);

INSERT INTO posts (uid, content) VALUES (1, 'Post user 1');
INSERT INTO posts (uid, content) VALUES (2, 'Post user 2');
INSERT INTO posts (uid, content) VALUES (3, 'E14a Hello Post');

DROP TABLE IF EXISTS follows;
CREATE TABLE follows (
    fid serial NOT NULL PRIMARY KEY,
    follower serial NOT NULL,
    following serial NOT NULL,
    FOREIGN KEY (follower) REFERENCES users(uid),
    FOREIGN KEY (following) REFERENCES users(uid)
);

INSERT INTO follows (follower, following) VALUES (1, 2);
INSERT INTO follows (follower, following) VALUES (2, 1);

DROP TABLE IF EXISTS likes;
CREATE TABLE likes (
    uid serial NOT NULL,
    pid serial NOT NULL,
    FOREIGN KEY (uid) REFERENCES users(uid),
    FOREIGN KEY (pid) REFERENCES posts(pid),
    PRIMARY KEY (uid, pid)
);