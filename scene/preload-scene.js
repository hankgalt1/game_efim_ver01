// @ts-ignore
import phaser from '../phaser.js';
import { SCENE_KEYS } from '../scene-keys.js';
import {GameScen} from '../scene/game_scene.js'


export class PreloadScene extends Phaser.Scene{
    constructor(){
        super({
            // @ts-ignore
            key:SCENE_KEYS.PRELOAD_SCENE,
            active:true
        });
        console.log('Загрузочная сцена');
    }
    
//Функция для переменных загрузочного экрана.  
    init(){
        this.telegram_info = window.Telegram.WebApp.WebAppInitData.query_id
        console.log('init')
        this.Trak_image = './preloader_window/png/'
        this.pre = 0
        this.url = new URL(location.href, location.origin);
        console.log(this.url)
        this.screenCenterX = this.cameras.main.worldView.x + this.cameras.main.width / 2;
        this.screenCenterY = this.cameras.main.worldView.y + this.cameras.main.height / 2;

    }
//Функция для загрузки ресурсов для загрузочного экрана.
    preload(){
        console.log('preload')
        this.load.image('bg',`${this.Trak_image}bg_preloader.png`)
        this.load.image('coin',`${this.Trak_image}icon_efimcoin.png`)
        this.load.image('preloader',`${this.Trak_image}loading_preloader.png`)
        
        

        

    }
//Функция для создания на кэнвасе объектов загрузочного экрана.
    create(){
        console.log('create')
        this.add.image(-4,-4,'bg').setOrigin(0).setDisplaySize(this.scale.width+4,this.scale.height+4)

        this.add.image(this.scale.width/2,this.scale.height/2/1.25,'coin').setDisplaySize(this.scale.width/1.5,this.scale.width/1.5)

        //this.preloader_igm = this.add.image(this.scale.width/2,this.scale.height/1.1,'preloader').setScale(1,0.3)
        this.Name_Preload_text =this.add.text(this.screenCenterX,this.scale.height/1.5, `${this.telegram_info}`, {
            font: `600 10px font1`,
            color:'#793b24' 
        }).setOrigin(0.5);;
        

        this.preload_text = this.add.text(this.screenCenterX,-50, `Загрузка`, {
            font: `600 ${this.scale.width/15}px font1`,
            color:'#000000' 
        }).setOrigin(0.5);


        //this.add.rectangle(this.scale.width/2-this.scale.width/2+20, this.scale.height/1.1, 10, 150, 0x37c3be)

        

        this.add.container(0, this.scale.height/1.05,[
            

            this.preload_text,
            //this.preloader_igm = this.add.image(this.screenCenterX,0,'preloader').setDisplaySize(this.scale.width-this.scale.width/10,this.scale.height/20),
            
            this.recting = this.add.rectangle(
            this.scale.width/20,
            0,
            0,
            this.scale.height/20-8 ,
            0xffd952),




            
                

            


        ]);

        
        
        
       

        
    }
//Функция для обновления данных загрузочного экрана.
    update(){
        this.pre++
        if (this.pre < this.scale.width-this.scale.width/20*2 ){
            this.recting.width++
            //console.log(this.recting.width)
            //console.log(this.pre)

        };
        this.start_game = false
        if (this.pre >= this.scale.width-this.scale.width/20*2 ){
            console.log("Start game")
            this.scene.start(SCENE_KEYS.GAME_SCENE, GameScen);

        };
        
        
            


        

        
        
        
    }
}
