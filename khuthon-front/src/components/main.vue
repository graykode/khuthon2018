<template>
    <div id="mainWrapper">
        <div id="section1">
            <searchFrom></searchFrom> 
            <wordcloud></wordcloud>
        </div>
        <div id="section2">
            <detail></detail>
        </div>
        <div id="section3">
            <comment></comment>
        </div>
    </div>
</template>

<script>
import eventBus from '../commons/eventBus'

import searchFrom from './searchForm'
import wordcloud from './wordcloud'
import comment from './comment'
import detail from './detail'

export default {
    created(){
        eventBus.$on("submit", (data)=>{
            console.log(data);
        })
    },
    components:{
        searchFrom,
        wordcloud,
        comment,
        detail
    },
    methods:{
        getDataFromServer(){
            
        }
    }
}
</script>

<style>
#mainWrapper{
    display: flex;
    flex-direction: row;
    justify-content: space-around;
    
    height: 100%;
    padding: 15px 30px;

    background-position: center;
    background-repeat: no-repeat;
    background-size: cover;

    /* background-image: url("../assets/background2.png"); */
    background: #64ee869a;
}
#section1{
    width: 45%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-between;
}
#section1 > :nth-child(1){
    height: 7%;
}
#section1 > :nth-child(2){
    height: 90%;
}
#section1 > *{
    box-shadow: 0 4px 8px 0 rgba(173, 75, 75, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
}
#section2{
    width: 25%;
}
#section3{
    width: 25%;
    box-shadow: 0 4px 8px 0 rgba(173, 75, 75, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
}

</style>
