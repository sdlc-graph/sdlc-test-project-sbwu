# Detailed Dog Art

```
                 __
        ,                    ," e`--o
       ((                   (  | __,`
        \\~----------------' \`;/
        (                      /
        /) ._______________.  )
       (( (               (( (
        ``-'               ``-`
```

* Set Min instances of the cloud run service to 1 , cpu to 8 and memory to 32GiB to avoid 502 errors.
* Deployed with cloud run source deploy.


The PR webhook events seem to work consistently now.

The test "ping" event that the webhook sends when you first set it up almost always fails with 502. 

`curl`ing with no payload works, with a large payload it also 502s. Even though the actual PR events sent from the webhook work. no idea
