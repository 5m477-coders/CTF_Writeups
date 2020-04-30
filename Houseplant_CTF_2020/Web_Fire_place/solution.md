# Web: Fire-place

## Challenge
> You see, I built a nice fire/place for us to all huddle around. It's completely decentralized, and we can all share stuff in it for fun!!
> Hint! I wonder... what's inside the HTML page?
> The HTML page: (fire-place[0].html)[fire-place[0].html]

## Solution
If you look at the source code, it’s using firebase’s filestore.\
I’ve got all the configs to access, so I’m free to get and update folders.\
I’ll write an extract code with reference to this.\

```javascript
<script type="text/javascript">
    var ref = db.collection("board").doc("data");
    ref.get().then((doc)=>{
        if (doc.exists) {
            console.log( doc.data() );
        }
        else {
            console.log("404");
        }
    })
    .catch( (error) => {
        console.log(`Could not get the data: (${error})`);
    });
</script> 
```

