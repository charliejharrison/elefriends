SELECT posts.id, posts.text
FROM posts
    LEFT JOIN content_flags
        ON content_flags.attachable_id = posts.id
    WHERE content_flags.attachable_id IS NULL