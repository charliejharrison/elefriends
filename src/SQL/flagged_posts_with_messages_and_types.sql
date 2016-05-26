SELECT posts.id post_id, content_flags.id flag_id, content_flaggings.id flagging_id, posts.text post_text, content_flag_types.name flag_type, content_flaggings.message flag_message
FROM content_flaggings
        INNER JOIN content_flag_types
                ON content_flaggings.content_flag_type_id = content_flag_types.id
        INNER JOIN content_flags 
                ON content_flaggings.content_flag_id = content_flags.id
        INNER JOIN posts
                ON content_flags.attachable_id = posts.id
        WHERE content_flags.attachable_type = 'Post'