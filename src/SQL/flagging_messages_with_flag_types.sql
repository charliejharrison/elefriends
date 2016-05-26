SELECT content_flag_types.name, content_flaggings.message, content_flaggings.id
FROM content_flaggings
INNER JOIN content_flag_types
ON content_flaggings.content_flag_type_id = content_flag_types.id