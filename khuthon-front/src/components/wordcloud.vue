<template>
    <div id="wordcloudWrapper">
        <wordcloud
            :data= "defaultWords"
            :rotate = "{ from: -0, to: 0, numOfOrientation: 1 }"
            nameKey = "name"
            valueKey = "value"
            :wordClick = this.wordClick
            fontScale = "log"
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
    created(){
        eventBus.$emit("createCloud");

        eventBus.$on("getWord",(data)=>{
            console.log("getword", data);
            this.defaultWords = [];
            this.wordsData = data;

            for(let index in this.wordsData){
                console.log("!");
                this.defaultWords.push({
                    name : this.wordsData[index].store_name,
                    value : this.wordsData[index].num,
                });
            }
        });
    },
    data() {
        return {
            wordsData: [],
            defaultWords: [],
        }
    },
    methods:{
        wordClick(text, vm){
            for(let index in this.wordsData){
                if(this.wordsData[index].store_name === text){
                    eventBus.$emit("wordClick", this.wordsData[index].id);
                    return;
                }
            }
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
