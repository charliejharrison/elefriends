SELECT posts.id post_id, posts.text post_text
FROM posts
        INNER JOIN content_flags
                ON content_flags.attachable_id = posts.id
        WHERE content_flags.attachable_type = 'Post'