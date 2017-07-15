/**
 * Created by PRIMUS on 2017/6/26.
 */


KindEditor.ready(function(K) {
                window.editor = K.create('textarea[name="bz"]', {
                        height:"200px",
                        width:"800px",
                        uploadJson:'/admin/upload/kindeditor'
                    });

        });



