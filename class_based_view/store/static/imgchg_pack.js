/*
 * �摜�؂�ւ�����
 * (c) Crytus 2015/12/25
 */
eval(function(p,a,c,k,e,r){e=function(c){return(c<a?'':e(parseInt(c/a)))+((c=c%a)>35?String.fromCharCode(c+29):c.toString(36))};if(!''.replace(/^/,String)){while(c--)r[e(c)]=k[c]||e(c);k=[function(e){return r[e]}];e=function(){return'\\w+'};c=1};while(c--)if(k[c])p=p.replace(new RegExp('\\b'+e(c)+'\\b','g'),k[c]);return p}('f x=0;f U=z;f 1c=-1;f C=1;f r=1d;f l=10;f D=(C*z)/r;f e;f k;f A;s V(v){d(v<=r){f t=a.b(k).W;f u=a.b(k).X;f m=v*t/r;f n=v*u/r;d(l==1){a.b(e).c.o=(m-t)+\'g\';a.b(k).c.o=m+\'g\'}h d(l==2){a.b(e).c.o=(m-t)+\'g\'}h d(l==3){a.b(e).c.o=(t-m)+\'g\';a.b(k).c.o=-m+\'g\'}h d(l==4){a.b(e).c.o=(t-m)+\'g\'}h d(l==5){a.b(e).c.p=(n-u)+\'g\';a.b(k).c.p=n+\'g\'}h d(l==6){a.b(e).c.p=(n-u)+\'g\'}h d(l==7){a.b(e).c.p=(u-n)+\'g\';a.b(k).c.p=-n+\'g\'}h d(l==8){a.b(e).c.p=(u-n)+\'g\'}h d(l==9){a.b(e).c.W=m+\'g\';a.b(e).c.X=n+\'g\';Y=(t-m)/2;Z=(u-n)/2;a.b(e).c.o=Y+\'g\';a.b(e).c.p=Z+\'g\'}h{d(a.K){a.b(e).c.L=\'M(y=\'+(v*z/r)+\')\'}h{a.b(e).c.y=1e(v)/r}}d(l!=10){d(a.K){a.b(e).c.L=\'M(y=z)\'}h{a.b(e).c.y=1.0}}}}s N(){V(x);x+=1;d(x>=U){a.b(k).q=a.b(e).q;a.b(k).c.o=\'E\';a.b(k).c.p=\'E\'}h{11(\'N()\',D)}}s O(F,w){d(a.b(k).q==F){P}d(x){a.b(k).q=a.b(e).q;a.b(k).c.o=\'E\';a.b(k).c.p=\'E\'}a.b(e).q=F;x=0;d(a.K){a.b(e).c.L=\'M(y=0)\'}h{a.b(e).c.y=0}d((A!=\'\')&&(w!=G)&&(w!=\'\')){a.b(A).1f=w}11(\'N()\',D)}s 12(Q){d(a.13){P a.13(Q)}f H=[];f I=a.1g(\'F\');R(f i=0;i<I.1h;i++){f S=I[i].H.1i(\' \');R(f j 14 S){d(S[j]==Q){H.1j(I[i])}}}P H}s 1k(15,16,17,w,J){f B=12(17);e=15;k=16;d(w!=G){A=w}h{A=\'\'}d(J!=G){C=J;D=(J*z)/r}h{C=2}R(i 14 B){d(B[i].q!=G){d(a.18){B[i].18("1l",s(){O(19.q,19.1a)},1m)}h{B[i].1n("1o",s(1b){f T=1b.1p;O(T.q,T.1a)})}}}}',62,88,'||||||||||document|getElementById|style|if|imgchg_image1|var|px|else|||imgchg_image2|imgchg_func|dw|dh|left|top|src|imgchg_step|function|max_width|max_height||caption|imgchg_count|opacity|100|imgchg_caption|imgary|imgchg_speed|imgchg_tick|0px|img|undefined|className|allElements|speed|all|filter|alpha|imgchg_timefunc|change_image|return|cls|for|ary|_this|imgchg_end|imgchg_change|width|height|xw|xh||setTimeout|getAllClass|getElementsByClassName|in|img1|img2|thumb|addEventListener|this|alt|evt|imgchg_loop_counter|40|parseFloat|innerHTML|getElementsByTagName|length|split|push|imgchg_start|click|false|attachEvent|onclick|srcElement'.split('|'),0,{}))


function open_accordion(hdr, item)
{
    var e = document.getElementById(hdr);
    var e2 = document.getElementById(item);
    e.addEventListener("click", function() { do_onoffaccordion(hdr, item); }, false);

    classList(e).remove('open');
    classList(e).add('close');
    if (classList(e).contains('open')) {
    // e.style.display = '';
        e2.style.display = '';
    }
    if (classList(e).contains('close')) {
    // e.style.display = '';
        e2.style.display = 'none';
    }
}