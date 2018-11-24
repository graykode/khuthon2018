<template>
    <div id="commentWrapper">
        <div class="comment" v-for="comment in comments" :key="comment.comment_id">
            <div>
                <i class="fas fa-user-circle" v-bind:class="{'male' : comment.gender==0, 'female' : comment.gender==1}"></i>
                <div> {{comment.user}} </div>
            </div>
            <div>
                <div>
                    {{comment.comment}}
                </div>
                <div>
                    Text-CNN 추정 평점 : {{comment.rating}}
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import eventBus from '../commons/eventBus'
export default {
    created(){
        eventBus.$on('getCommend',(data)=>{
            this.comments = data.data.comments;
        });
    },
    data(){
        return{
            comments : [
            ]
        }
    }
}
</script>

<style>
::-webkit-scrollbar { 
    display: none; 
}
#commentWrapper{
    height: 100%;
    background: #ffffff;
 
    overflow: scroll;
}
.comment{
    margin: 0 auto;

    display: flex;
    flex-direction: row;
    justify-content: space-around;
    align-items: center;

    margin-top: 15px;
    width: 90%;
    box-shadow: 0 4px 8px 0 rgba(173, 75, 75, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
}
.comment > :nth-child(1){
    width: 20%;
    margin: 15px;
    font-size: 12px;

    display: flex;
    flex-direction: column;
    align-items: center;
}
.comment > :nth-child(2){
    text-align: start;
    font-size: 10px;
}
.comment > :nth-child(2) > div{
    margin: 10px;
}
.comment > :nth-child(2) > div:nth-child(2){
    font-size: 13px;
    color:#a8a8a8;
}
.fa-user-circle{
    font-size: 60px;
}
.male{
    color: #00ffff;
}
.female{
    color: #ff00aa;
}

.comment > :nth-child(2){
    width: 70%;

    display: flex;
    flex-direction: column;
}

</style>
