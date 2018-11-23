<template>
    <div id="wordcloudWrapper">
        <wordcloud
            :data="defaultWords"
            :rotate = "{ from: -0, to: 0, numOfOrientation: 1 }"
            nameKey ="name"
            valueKey ="value"
        >
        </wordcloud>
    </div>
</template>

<script>
import wordcloud from 'vue-wordcloud'

export default {
    name: 'app',
    components: {
        wordcloud
    },
    data() {
        return {
            defaultWords: [{
          "name": "Cat",
          "value": 26
        },
        {
          "name": "fish",
          "value": 19
        },
        {
          "name": "things",
          "value": 18
        },
        {
          "name": "look",
          "value": 16
        },
        {
          "name": "two",
          "value": 15
        },
        {
          "name": "fun",
          "value": 9
        },
        {
          "name": "know",
          "value": 9
        },
        {
          "name": "good",
          "value": 9
        },
        {
          "name": "play",
          "value": 6
        }
      ]
        }
    },
    methods:{
        addWords(name, value){
            this.defaultWords.push({
                name,
                value
            })
        }
    }
}
</script>

<style>
#wordcloudWrapper{
    width:100%;
    background: #ffffff;
}
</style>
