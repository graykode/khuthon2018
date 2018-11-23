<template>
    <div id="wordcloudWrapper">
        <wordcloud
            :data="defaultWords"
            :rotate = "{ from: -0, to: 0, numOfOrientation: 2 }"
            nameKey ="name"
            valueKey ="value"
            :wordClick = this.wordClick
        >
        </wordcloud>
    </div>
</template>

<script>
import eventBus from '../commons/eventBus'
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
        },
        wordClick(text, vm){
            eventBus.$emit("wordClick", text);
        }
    }
}
</script>

<style>
#wordcloudWrapper{
    display: flex;
    justify-content: center;
    align-items: center;
    width:100%;
    background: #ffffff;
}
</style>
