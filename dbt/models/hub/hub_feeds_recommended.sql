SELECT vos_details.id,
       vos_details.title,
       vos_details.subTitle,
       vos_details.date,
       vos_details.webLink,
       vos_details.detectedLanguage,
       vos_details.likeCount,
       vos_details.shareCount,
       vos_details.viewCount,
       vos_details.authorIsVerified,
       vos_details.authorName
FROM (SELECT code,
             message,
             explode(data.vos) AS vos_details
      FROM {{ ref("raw_feeds_recommended") }}) AS exploded_data
WHERE vos_details.title is not null