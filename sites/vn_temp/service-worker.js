"use strict";

var version = 'v2::';

self.addEventListener('install', function(event) {
	event.waitUntil(
    	caches.open(version + '-cache').then(function(cache) {
			return cache.addAll(
        	[
				'/sites/vn_temp/999.html',
				'/sites/vn_temp/Danganronpa.html',
				'/sites/vn_temp/index.html',
				'/sites/vn_temp/KatawaShoujo.html',
				'/sites/vn_temp/LittleBusters.html',
				'/sites/vn_temp/manifest.json',
				'/sites/vn_temp/PhoenixWright.html',
				'/sites/vn_temp/README.md',
				'/sites/vn_temp/service-worker.js',
				'/sites/vn_temp/SteinsGate.html',
				'/sites/vn_temp/css/999.css',
				'/sites/vn_temp/css/all.css',
				'/sites/vn_temp/css/bootstrap-theme.css',
				'/sites/vn_temp/css/bootstrap-theme.css.map',
				'/sites/vn_temp/css/bootstrap-theme.min.css',
				'/sites/vn_temp/css/bootstrap-theme.min.css.map',
				'/sites/vn_temp/css/bootstrap.css',
				'/sites/vn_temp/css/bootstrap.css.map',
				'/sites/vn_temp/css/bootstrap.min.css',
				'/sites/vn_temp/css/bootstrap.min.css.map',
				'/sites/vn_temp/css/Danganronpa.css',
				'/sites/vn_temp/css/docs.css',
				'/sites/vn_temp/css/docs.less',
				'/sites/vn_temp/css/fa-brands.css',
				'/sites/vn_temp/css/fa-brands.min.css',
				'/sites/vn_temp/css/fa-regular.css',
				'/sites/vn_temp/css/fa-regular.min.css',
				'/sites/vn_temp/css/fa-solid.css',
				'/sites/vn_temp/css/fa-solid.min.css',
				'/sites/vn_temp/css/fakeloader.css',
				'/sites/vn_temp/css/flag-icon.css',
				'/sites/vn_temp/css/flag-icon.min.css',
				'/sites/vn_temp/css/flickity.css',
				'/sites/vn_temp/css/font-awesome.css',
				'/sites/vn_temp/css/font-awesome.min.css',
				'/sites/vn_temp/css/fullscreen.css',
				'/sites/vn_temp/css/KatawaShoujo.css',
				'/sites/vn_temp/css/lightbox.css',
				'/sites/vn_temp/css/lightslider.css',
				'/sites/vn_temp/css/lightslider.min.css',
				'/sites/vn_temp/css/LittleBusters.css',
				'/sites/vn_temp/css/main.css',
				'/sites/vn_temp/css/PhoenixWright.css',
				'/sites/vn_temp/css/SteinsGate.css',
				'/sites/vn_temp/flags/1x1/ad.svg',
				'/sites/vn_temp/flags/1x1/ae.svg',
				'/sites/vn_temp/flags/1x1/af.svg',
				'/sites/vn_temp/flags/1x1/ag.svg',
				'/sites/vn_temp/flags/1x1/ai.svg',
				'/sites/vn_temp/flags/1x1/al.svg',
				'/sites/vn_temp/flags/1x1/am.svg',
				'/sites/vn_temp/flags/1x1/ao.svg',
				'/sites/vn_temp/flags/1x1/aq.svg',
				'/sites/vn_temp/flags/1x1/ar.svg',
				'/sites/vn_temp/flags/1x1/as.svg',
				'/sites/vn_temp/flags/1x1/at.svg',
				'/sites/vn_temp/flags/1x1/au.svg',
				'/sites/vn_temp/flags/1x1/aw.svg',
				'/sites/vn_temp/flags/1x1/ax.svg',
				'/sites/vn_temp/flags/1x1/az.svg',
				'/sites/vn_temp/flags/1x1/ba.svg',
				'/sites/vn_temp/flags/1x1/bb.svg',
				'/sites/vn_temp/flags/1x1/bd.svg',
				'/sites/vn_temp/flags/1x1/be.svg',
				'/sites/vn_temp/flags/1x1/bf.svg',
				'/sites/vn_temp/flags/1x1/bg.svg',
				'/sites/vn_temp/flags/1x1/bh.svg',
				'/sites/vn_temp/flags/1x1/bi.svg',
				'/sites/vn_temp/flags/1x1/bj.svg',
				'/sites/vn_temp/flags/1x1/bl.svg',
				'/sites/vn_temp/flags/1x1/bm.svg',
				'/sites/vn_temp/flags/1x1/bn.svg',
				'/sites/vn_temp/flags/1x1/bo.svg',
				'/sites/vn_temp/flags/1x1/bq.svg',
				'/sites/vn_temp/flags/1x1/br.svg',
				'/sites/vn_temp/flags/1x1/bs.svg',
				'/sites/vn_temp/flags/1x1/bt.svg',
				'/sites/vn_temp/flags/1x1/bv.svg',
				'/sites/vn_temp/flags/1x1/bw.svg',
				'/sites/vn_temp/flags/1x1/by.svg',
				'/sites/vn_temp/flags/1x1/bz.svg',
				'/sites/vn_temp/flags/1x1/ca.svg',
				'/sites/vn_temp/flags/1x1/cc.svg',
				'/sites/vn_temp/flags/1x1/cd.svg',
				'/sites/vn_temp/flags/1x1/cf.svg',
				'/sites/vn_temp/flags/1x1/cg.svg',
				'/sites/vn_temp/flags/1x1/ch.svg',
				'/sites/vn_temp/flags/1x1/ci.svg',
				'/sites/vn_temp/flags/1x1/ck.svg',
				'/sites/vn_temp/flags/1x1/cl.svg',
				'/sites/vn_temp/flags/1x1/cm.svg',
				'/sites/vn_temp/flags/1x1/cn.svg',
				'/sites/vn_temp/flags/1x1/co.svg',
				'/sites/vn_temp/flags/1x1/cr.svg',
				'/sites/vn_temp/flags/1x1/cu.svg',
				'/sites/vn_temp/flags/1x1/cv.svg',
				'/sites/vn_temp/flags/1x1/cw.svg',
				'/sites/vn_temp/flags/1x1/cx.svg',
				'/sites/vn_temp/flags/1x1/cy.svg',
				'/sites/vn_temp/flags/1x1/cz.svg',
				'/sites/vn_temp/flags/1x1/de.svg',
				'/sites/vn_temp/flags/1x1/dj.svg',
				'/sites/vn_temp/flags/1x1/dk.svg',
				'/sites/vn_temp/flags/1x1/dm.svg',
				'/sites/vn_temp/flags/1x1/do.svg',
				'/sites/vn_temp/flags/1x1/dz.svg',
				'/sites/vn_temp/flags/1x1/ec.svg',
				'/sites/vn_temp/flags/1x1/ee.svg',
				'/sites/vn_temp/flags/1x1/eg.svg',
				'/sites/vn_temp/flags/1x1/eh.svg',
				'/sites/vn_temp/flags/1x1/er.svg',
				'/sites/vn_temp/flags/1x1/es-ct.svg',
				'/sites/vn_temp/flags/1x1/es.svg',
				'/sites/vn_temp/flags/1x1/et.svg',
				'/sites/vn_temp/flags/1x1/eu.svg',
				'/sites/vn_temp/flags/1x1/fi.svg',
				'/sites/vn_temp/flags/1x1/fj.svg',
				'/sites/vn_temp/flags/1x1/fk.svg',
				'/sites/vn_temp/flags/1x1/fm.svg',
				'/sites/vn_temp/flags/1x1/fo.svg',
				'/sites/vn_temp/flags/1x1/fr.svg',
				'/sites/vn_temp/flags/1x1/ga.svg',
				'/sites/vn_temp/flags/1x1/gb-eng.svg',
				'/sites/vn_temp/flags/1x1/gb-nir.svg',
				'/sites/vn_temp/flags/1x1/gb-sct.svg',
				'/sites/vn_temp/flags/1x1/gb-wls.svg',
				'/sites/vn_temp/flags/1x1/gb.svg',
				'/sites/vn_temp/flags/1x1/gd.svg',
				'/sites/vn_temp/flags/1x1/ge.svg',
				'/sites/vn_temp/flags/1x1/gf.svg',
				'/sites/vn_temp/flags/1x1/gg.svg',
				'/sites/vn_temp/flags/1x1/gh.svg',
				'/sites/vn_temp/flags/1x1/gi.svg',
				'/sites/vn_temp/flags/1x1/gl.svg',
				'/sites/vn_temp/flags/1x1/gm.svg',
				'/sites/vn_temp/flags/1x1/gn.svg',
				'/sites/vn_temp/flags/1x1/gp.svg',
				'/sites/vn_temp/flags/1x1/gq.svg',
				'/sites/vn_temp/flags/1x1/gr.svg',
				'/sites/vn_temp/flags/1x1/gs.svg',
				'/sites/vn_temp/flags/1x1/gt.svg',
				'/sites/vn_temp/flags/1x1/gu.svg',
				'/sites/vn_temp/flags/1x1/gw.svg',
				'/sites/vn_temp/flags/1x1/gy.svg',
				'/sites/vn_temp/flags/1x1/hk.svg',
				'/sites/vn_temp/flags/1x1/hm.svg',
				'/sites/vn_temp/flags/1x1/hn.svg',
				'/sites/vn_temp/flags/1x1/hr.svg',
				'/sites/vn_temp/flags/1x1/ht.svg',
				'/sites/vn_temp/flags/1x1/hu.svg',
				'/sites/vn_temp/flags/1x1/id.svg',
				'/sites/vn_temp/flags/1x1/ie.svg',
				'/sites/vn_temp/flags/1x1/il.svg',
				'/sites/vn_temp/flags/1x1/im.svg',
				'/sites/vn_temp/flags/1x1/in.svg',
				'/sites/vn_temp/flags/1x1/io.svg',
				'/sites/vn_temp/flags/1x1/iq.svg',
				'/sites/vn_temp/flags/1x1/ir.svg',
				'/sites/vn_temp/flags/1x1/is.svg',
				'/sites/vn_temp/flags/1x1/it.svg',
				'/sites/vn_temp/flags/1x1/je.svg',
				'/sites/vn_temp/flags/1x1/jm.svg',
				'/sites/vn_temp/flags/1x1/jo.svg',
				'/sites/vn_temp/flags/1x1/jp.svg',
				'/sites/vn_temp/flags/1x1/ke.svg',
				'/sites/vn_temp/flags/1x1/kg.svg',
				'/sites/vn_temp/flags/1x1/kh.svg',
				'/sites/vn_temp/flags/1x1/ki.svg',
				'/sites/vn_temp/flags/1x1/km.svg',
				'/sites/vn_temp/flags/1x1/kn.svg',
				'/sites/vn_temp/flags/1x1/kp.svg',
				'/sites/vn_temp/flags/1x1/kr.svg',
				'/sites/vn_temp/flags/1x1/kw.svg',
				'/sites/vn_temp/flags/1x1/ky.svg',
				'/sites/vn_temp/flags/1x1/kz.svg',
				'/sites/vn_temp/flags/1x1/la.svg',
				'/sites/vn_temp/flags/1x1/lb.svg',
				'/sites/vn_temp/flags/1x1/lc.svg',
				'/sites/vn_temp/flags/1x1/li.svg',
				'/sites/vn_temp/flags/1x1/lk.svg',
				'/sites/vn_temp/flags/1x1/lr.svg',
				'/sites/vn_temp/flags/1x1/ls.svg',
				'/sites/vn_temp/flags/1x1/lt.svg',
				'/sites/vn_temp/flags/1x1/lu.svg',
				'/sites/vn_temp/flags/1x1/lv.svg',
				'/sites/vn_temp/flags/1x1/ly.svg',
				'/sites/vn_temp/flags/1x1/ma.svg',
				'/sites/vn_temp/flags/1x1/mc.svg',
				'/sites/vn_temp/flags/1x1/md.svg',
				'/sites/vn_temp/flags/1x1/me.svg',
				'/sites/vn_temp/flags/1x1/mf.svg',
				'/sites/vn_temp/flags/1x1/mg.svg',
				'/sites/vn_temp/flags/1x1/mh.svg',
				'/sites/vn_temp/flags/1x1/mk.svg',
				'/sites/vn_temp/flags/1x1/ml.svg',
				'/sites/vn_temp/flags/1x1/mm.svg',
				'/sites/vn_temp/flags/1x1/mn.svg',
				'/sites/vn_temp/flags/1x1/mo.svg',
				'/sites/vn_temp/flags/1x1/mp.svg',
				'/sites/vn_temp/flags/1x1/mq.svg',
				'/sites/vn_temp/flags/1x1/mr.svg',
				'/sites/vn_temp/flags/1x1/ms.svg',
				'/sites/vn_temp/flags/1x1/mt.svg',
				'/sites/vn_temp/flags/1x1/mu.svg',
				'/sites/vn_temp/flags/1x1/mv.svg',
				'/sites/vn_temp/flags/1x1/mw.svg',
				'/sites/vn_temp/flags/1x1/mx.svg',
				'/sites/vn_temp/flags/1x1/my.svg',
				'/sites/vn_temp/flags/1x1/mz.svg',
				'/sites/vn_temp/flags/1x1/na.svg',
				'/sites/vn_temp/flags/1x1/nc.svg',
				'/sites/vn_temp/flags/1x1/ne.svg',
				'/sites/vn_temp/flags/1x1/nf.svg',
				'/sites/vn_temp/flags/1x1/ng.svg',
				'/sites/vn_temp/flags/1x1/ni.svg',
				'/sites/vn_temp/flags/1x1/nl.svg',
				'/sites/vn_temp/flags/1x1/no.svg',
				'/sites/vn_temp/flags/1x1/np.svg',
				'/sites/vn_temp/flags/1x1/nr.svg',
				'/sites/vn_temp/flags/1x1/nu.svg',
				'/sites/vn_temp/flags/1x1/nz.svg',
				'/sites/vn_temp/flags/1x1/om.svg',
				'/sites/vn_temp/flags/1x1/pa.svg',
				'/sites/vn_temp/flags/1x1/pe.svg',
				'/sites/vn_temp/flags/1x1/pf.svg',
				'/sites/vn_temp/flags/1x1/pg.svg',
				'/sites/vn_temp/flags/1x1/ph.svg',
				'/sites/vn_temp/flags/1x1/pk.svg',
				'/sites/vn_temp/flags/1x1/pl.svg',
				'/sites/vn_temp/flags/1x1/pm.svg',
				'/sites/vn_temp/flags/1x1/pn.svg',
				'/sites/vn_temp/flags/1x1/pr.svg',
				'/sites/vn_temp/flags/1x1/ps.svg',
				'/sites/vn_temp/flags/1x1/pt.svg',
				'/sites/vn_temp/flags/1x1/pw.svg',
				'/sites/vn_temp/flags/1x1/py.svg',
				'/sites/vn_temp/flags/1x1/qa.svg',
				'/sites/vn_temp/flags/1x1/re.svg',
				'/sites/vn_temp/flags/1x1/ro.svg',
				'/sites/vn_temp/flags/1x1/rs.svg',
				'/sites/vn_temp/flags/1x1/ru.svg',
				'/sites/vn_temp/flags/1x1/rw.svg',
				'/sites/vn_temp/flags/1x1/sa.svg',
				'/sites/vn_temp/flags/1x1/sb.svg',
				'/sites/vn_temp/flags/1x1/sc.svg',
				'/sites/vn_temp/flags/1x1/sd.svg',
				'/sites/vn_temp/flags/1x1/se.svg',
				'/sites/vn_temp/flags/1x1/sg.svg',
				'/sites/vn_temp/flags/1x1/sh.svg',
				'/sites/vn_temp/flags/1x1/si.svg',
				'/sites/vn_temp/flags/1x1/sj.svg',
				'/sites/vn_temp/flags/1x1/sk.svg',
				'/sites/vn_temp/flags/1x1/sl.svg',
				'/sites/vn_temp/flags/1x1/sm.svg',
				'/sites/vn_temp/flags/1x1/sn.svg',
				'/sites/vn_temp/flags/1x1/so.svg',
				'/sites/vn_temp/flags/1x1/sr.svg',
				'/sites/vn_temp/flags/1x1/ss.svg',
				'/sites/vn_temp/flags/1x1/st.svg',
				'/sites/vn_temp/flags/1x1/sv.svg',
				'/sites/vn_temp/flags/1x1/sx.svg',
				'/sites/vn_temp/flags/1x1/sy.svg',
				'/sites/vn_temp/flags/1x1/sz.svg',
				'/sites/vn_temp/flags/1x1/tc.svg',
				'/sites/vn_temp/flags/1x1/td.svg',
				'/sites/vn_temp/flags/1x1/tf.svg',
				'/sites/vn_temp/flags/1x1/tg.svg',
				'/sites/vn_temp/flags/1x1/th.svg',
				'/sites/vn_temp/flags/1x1/tj.svg',
				'/sites/vn_temp/flags/1x1/tk.svg',
				'/sites/vn_temp/flags/1x1/tl.svg',
				'/sites/vn_temp/flags/1x1/tm.svg',
				'/sites/vn_temp/flags/1x1/tn.svg',
				'/sites/vn_temp/flags/1x1/to.svg',
				'/sites/vn_temp/flags/1x1/tr.svg',
				'/sites/vn_temp/flags/1x1/tt.svg',
				'/sites/vn_temp/flags/1x1/tv.svg',
				'/sites/vn_temp/flags/1x1/tw.svg',
				'/sites/vn_temp/flags/1x1/tz.svg',
				'/sites/vn_temp/flags/1x1/ua.svg',
				'/sites/vn_temp/flags/1x1/ug.svg',
				'/sites/vn_temp/flags/1x1/um.svg',
				'/sites/vn_temp/flags/1x1/un.svg',
				'/sites/vn_temp/flags/1x1/us.svg',
				'/sites/vn_temp/flags/1x1/uy.svg',
				'/sites/vn_temp/flags/1x1/uz.svg',
				'/sites/vn_temp/flags/1x1/va.svg',
				'/sites/vn_temp/flags/1x1/vc.svg',
				'/sites/vn_temp/flags/1x1/ve.svg',
				'/sites/vn_temp/flags/1x1/vg.svg',
				'/sites/vn_temp/flags/1x1/vi.svg',
				'/sites/vn_temp/flags/1x1/vn.svg',
				'/sites/vn_temp/flags/1x1/vu.svg',
				'/sites/vn_temp/flags/1x1/wf.svg',
				'/sites/vn_temp/flags/1x1/ws.svg',
				'/sites/vn_temp/flags/1x1/ye.svg',
				'/sites/vn_temp/flags/1x1/yt.svg',
				'/sites/vn_temp/flags/1x1/za.svg',
				'/sites/vn_temp/flags/1x1/zm.svg',
				'/sites/vn_temp/flags/1x1/zw.svg',
				'/sites/vn_temp/flags/4x3/ad.svg',
				'/sites/vn_temp/flags/4x3/ae.svg',
				'/sites/vn_temp/flags/4x3/af.svg',
				'/sites/vn_temp/flags/4x3/ag.svg',
				'/sites/vn_temp/flags/4x3/ai.svg',
				'/sites/vn_temp/flags/4x3/al.svg',
				'/sites/vn_temp/flags/4x3/am.svg',
				'/sites/vn_temp/flags/4x3/ao.svg',
				'/sites/vn_temp/flags/4x3/aq.svg',
				'/sites/vn_temp/flags/4x3/ar.svg',
				'/sites/vn_temp/flags/4x3/as.svg',
				'/sites/vn_temp/flags/4x3/at.svg',
				'/sites/vn_temp/flags/4x3/au.svg',
				'/sites/vn_temp/flags/4x3/aw.svg',
				'/sites/vn_temp/flags/4x3/ax.svg',
				'/sites/vn_temp/flags/4x3/az.svg',
				'/sites/vn_temp/flags/4x3/ba.svg',
				'/sites/vn_temp/flags/4x3/bb.svg',
				'/sites/vn_temp/flags/4x3/bd.svg',
				'/sites/vn_temp/flags/4x3/be.svg',
				'/sites/vn_temp/flags/4x3/bf.svg',
				'/sites/vn_temp/flags/4x3/bg.svg',
				'/sites/vn_temp/flags/4x3/bh.svg',
				'/sites/vn_temp/flags/4x3/bi.svg',
				'/sites/vn_temp/flags/4x3/bj.svg',
				'/sites/vn_temp/flags/4x3/bl.svg',
				'/sites/vn_temp/flags/4x3/bm.svg',
				'/sites/vn_temp/flags/4x3/bn.svg',
				'/sites/vn_temp/flags/4x3/bo.svg',
				'/sites/vn_temp/flags/4x3/bq.svg',
				'/sites/vn_temp/flags/4x3/br.svg',
				'/sites/vn_temp/flags/4x3/bs.svg',
				'/sites/vn_temp/flags/4x3/bt.svg',
				'/sites/vn_temp/flags/4x3/bv.svg',
				'/sites/vn_temp/flags/4x3/bw.svg',
				'/sites/vn_temp/flags/4x3/by.svg',
				'/sites/vn_temp/flags/4x3/bz.svg',
				'/sites/vn_temp/flags/4x3/ca.svg',
				'/sites/vn_temp/flags/4x3/cc.svg',
				'/sites/vn_temp/flags/4x3/cd.svg',
				'/sites/vn_temp/flags/4x3/cf.svg',
				'/sites/vn_temp/flags/4x3/cg.svg',
				'/sites/vn_temp/flags/4x3/ch.svg',
				'/sites/vn_temp/flags/4x3/ci.svg',
				'/sites/vn_temp/flags/4x3/ck.svg',
				'/sites/vn_temp/flags/4x3/cl.svg',
				'/sites/vn_temp/flags/4x3/cm.svg',
				'/sites/vn_temp/flags/4x3/cn.svg',
				'/sites/vn_temp/flags/4x3/co.svg',
				'/sites/vn_temp/flags/4x3/cr.svg',
				'/sites/vn_temp/flags/4x3/cu.svg',
				'/sites/vn_temp/flags/4x3/cv.svg',
				'/sites/vn_temp/flags/4x3/cw.svg',
				'/sites/vn_temp/flags/4x3/cx.svg',
				'/sites/vn_temp/flags/4x3/cy.svg',
				'/sites/vn_temp/flags/4x3/cz.svg',
				'/sites/vn_temp/flags/4x3/de.svg',
				'/sites/vn_temp/flags/4x3/dj.svg',
				'/sites/vn_temp/flags/4x3/dk.svg',
				'/sites/vn_temp/flags/4x3/dm.svg',
				'/sites/vn_temp/flags/4x3/do.svg',
				'/sites/vn_temp/flags/4x3/dz.svg',
				'/sites/vn_temp/flags/4x3/ec.svg',
				'/sites/vn_temp/flags/4x3/ee.svg',
				'/sites/vn_temp/flags/4x3/eg.svg',
				'/sites/vn_temp/flags/4x3/eh.svg',
				'/sites/vn_temp/flags/4x3/er.svg',
				'/sites/vn_temp/flags/4x3/es-ct.svg',
				'/sites/vn_temp/flags/4x3/es.svg',
				'/sites/vn_temp/flags/4x3/et.svg',
				'/sites/vn_temp/flags/4x3/eu.svg',
				'/sites/vn_temp/flags/4x3/fi.svg',
				'/sites/vn_temp/flags/4x3/fj.svg',
				'/sites/vn_temp/flags/4x3/fk.svg',
				'/sites/vn_temp/flags/4x3/fm.svg',
				'/sites/vn_temp/flags/4x3/fo.svg',
				'/sites/vn_temp/flags/4x3/fr.svg',
				'/sites/vn_temp/flags/4x3/ga.svg',
				'/sites/vn_temp/flags/4x3/gb-eng.svg',
				'/sites/vn_temp/flags/4x3/gb-nir.svg',
				'/sites/vn_temp/flags/4x3/gb-sct.svg',
				'/sites/vn_temp/flags/4x3/gb-wls.svg',
				'/sites/vn_temp/flags/4x3/gb.svg',
				'/sites/vn_temp/flags/4x3/gd.svg',
				'/sites/vn_temp/flags/4x3/ge.svg',
				'/sites/vn_temp/flags/4x3/gf.svg',
				'/sites/vn_temp/flags/4x3/gg.svg',
				'/sites/vn_temp/flags/4x3/gh.svg',
				'/sites/vn_temp/flags/4x3/gi.svg',
				'/sites/vn_temp/flags/4x3/gl.svg',
				'/sites/vn_temp/flags/4x3/gm.svg',
				'/sites/vn_temp/flags/4x3/gn.svg',
				'/sites/vn_temp/flags/4x3/gp.svg',
				'/sites/vn_temp/flags/4x3/gq.svg',
				'/sites/vn_temp/flags/4x3/gr.svg',
				'/sites/vn_temp/flags/4x3/gs.svg',
				'/sites/vn_temp/flags/4x3/gt.svg',
				'/sites/vn_temp/flags/4x3/gu.svg',
				'/sites/vn_temp/flags/4x3/gw.svg',
				'/sites/vn_temp/flags/4x3/gy.svg',
				'/sites/vn_temp/flags/4x3/hk.svg',
				'/sites/vn_temp/flags/4x3/hm.svg',
				'/sites/vn_temp/flags/4x3/hn.svg',
				'/sites/vn_temp/flags/4x3/hr.svg',
				'/sites/vn_temp/flags/4x3/ht.svg',
				'/sites/vn_temp/flags/4x3/hu.svg',
				'/sites/vn_temp/flags/4x3/id.svg',
				'/sites/vn_temp/flags/4x3/ie.svg',
				'/sites/vn_temp/flags/4x3/il.svg',
				'/sites/vn_temp/flags/4x3/im.svg',
				'/sites/vn_temp/flags/4x3/in.svg',
				'/sites/vn_temp/flags/4x3/io.svg',
				'/sites/vn_temp/flags/4x3/iq.svg',
				'/sites/vn_temp/flags/4x3/ir.svg',
				'/sites/vn_temp/flags/4x3/is.svg',
				'/sites/vn_temp/flags/4x3/it.svg',
				'/sites/vn_temp/flags/4x3/je.svg',
				'/sites/vn_temp/flags/4x3/jm.svg',
				'/sites/vn_temp/flags/4x3/jo.svg',
				'/sites/vn_temp/flags/4x3/jp.svg',
				'/sites/vn_temp/flags/4x3/ke.svg',
				'/sites/vn_temp/flags/4x3/kg.svg',
				'/sites/vn_temp/flags/4x3/kh.svg',
				'/sites/vn_temp/flags/4x3/ki.svg',
				'/sites/vn_temp/flags/4x3/km.svg',
				'/sites/vn_temp/flags/4x3/kn.svg',
				'/sites/vn_temp/flags/4x3/kp.svg',
				'/sites/vn_temp/flags/4x3/kr.svg',
				'/sites/vn_temp/flags/4x3/kw.svg',
				'/sites/vn_temp/flags/4x3/ky.svg',
				'/sites/vn_temp/flags/4x3/kz.svg',
				'/sites/vn_temp/flags/4x3/la.svg',
				'/sites/vn_temp/flags/4x3/lb.svg',
				'/sites/vn_temp/flags/4x3/lc.svg',
				'/sites/vn_temp/flags/4x3/li.svg',
				'/sites/vn_temp/flags/4x3/lk.svg',
				'/sites/vn_temp/flags/4x3/lr.svg',
				'/sites/vn_temp/flags/4x3/ls.svg',
				'/sites/vn_temp/flags/4x3/lt.svg',
				'/sites/vn_temp/flags/4x3/lu.svg',
				'/sites/vn_temp/flags/4x3/lv.svg',
				'/sites/vn_temp/flags/4x3/ly.svg',
				'/sites/vn_temp/flags/4x3/ma.svg',
				'/sites/vn_temp/flags/4x3/mc.svg',
				'/sites/vn_temp/flags/4x3/md.svg',
				'/sites/vn_temp/flags/4x3/me.svg',
				'/sites/vn_temp/flags/4x3/mf.svg',
				'/sites/vn_temp/flags/4x3/mg.svg',
				'/sites/vn_temp/flags/4x3/mh.svg',
				'/sites/vn_temp/flags/4x3/mk.svg',
				'/sites/vn_temp/flags/4x3/ml.svg',
				'/sites/vn_temp/flags/4x3/mm.svg',
				'/sites/vn_temp/flags/4x3/mn.svg',
				'/sites/vn_temp/flags/4x3/mo.svg',
				'/sites/vn_temp/flags/4x3/mp.svg',
				'/sites/vn_temp/flags/4x3/mq.svg',
				'/sites/vn_temp/flags/4x3/mr.svg',
				'/sites/vn_temp/flags/4x3/ms.svg',
				'/sites/vn_temp/flags/4x3/mt.svg',
				'/sites/vn_temp/flags/4x3/mu.svg',
				'/sites/vn_temp/flags/4x3/mv.svg',
				'/sites/vn_temp/flags/4x3/mw.svg',
				'/sites/vn_temp/flags/4x3/mx.svg',
				'/sites/vn_temp/flags/4x3/my.svg',
				'/sites/vn_temp/flags/4x3/mz.svg',
				'/sites/vn_temp/flags/4x3/na.svg',
				'/sites/vn_temp/flags/4x3/nc.svg',
				'/sites/vn_temp/flags/4x3/ne.svg',
				'/sites/vn_temp/flags/4x3/nf.svg',
				'/sites/vn_temp/flags/4x3/ng.svg',
				'/sites/vn_temp/flags/4x3/ni.svg',
				'/sites/vn_temp/flags/4x3/nl.svg',
				'/sites/vn_temp/flags/4x3/no.svg',
				'/sites/vn_temp/flags/4x3/np.svg',
				'/sites/vn_temp/flags/4x3/nr.svg',
				'/sites/vn_temp/flags/4x3/nu.svg',
				'/sites/vn_temp/flags/4x3/nz.svg',
				'/sites/vn_temp/flags/4x3/om.svg',
				'/sites/vn_temp/flags/4x3/pa.svg',
				'/sites/vn_temp/flags/4x3/pe.svg',
				'/sites/vn_temp/flags/4x3/pf.svg',
				'/sites/vn_temp/flags/4x3/pg.svg',
				'/sites/vn_temp/flags/4x3/ph.svg',
				'/sites/vn_temp/flags/4x3/pk.svg',
				'/sites/vn_temp/flags/4x3/pl.svg',
				'/sites/vn_temp/flags/4x3/pm.svg',
				'/sites/vn_temp/flags/4x3/pn.svg',
				'/sites/vn_temp/flags/4x3/pr.svg',
				'/sites/vn_temp/flags/4x3/ps.svg',
				'/sites/vn_temp/flags/4x3/pt.svg',
				'/sites/vn_temp/flags/4x3/pw.svg',
				'/sites/vn_temp/flags/4x3/py.svg',
				'/sites/vn_temp/flags/4x3/qa.svg',
				'/sites/vn_temp/flags/4x3/re.svg',
				'/sites/vn_temp/flags/4x3/ro.svg',
				'/sites/vn_temp/flags/4x3/rs.svg',
				'/sites/vn_temp/flags/4x3/ru.svg',
				'/sites/vn_temp/flags/4x3/rw.svg',
				'/sites/vn_temp/flags/4x3/sa.svg',
				'/sites/vn_temp/flags/4x3/sb.svg',
				'/sites/vn_temp/flags/4x3/sc.svg',
				'/sites/vn_temp/flags/4x3/sd.svg',
				'/sites/vn_temp/flags/4x3/se.svg',
				'/sites/vn_temp/flags/4x3/sg.svg',
				'/sites/vn_temp/flags/4x3/sh.svg',
				'/sites/vn_temp/flags/4x3/si.svg',
				'/sites/vn_temp/flags/4x3/sj.svg',
				'/sites/vn_temp/flags/4x3/sk.svg',
				'/sites/vn_temp/flags/4x3/sl.svg',
				'/sites/vn_temp/flags/4x3/sm.svg',
				'/sites/vn_temp/flags/4x3/sn.svg',
				'/sites/vn_temp/flags/4x3/so.svg',
				'/sites/vn_temp/flags/4x3/sr.svg',
				'/sites/vn_temp/flags/4x3/ss.svg',
				'/sites/vn_temp/flags/4x3/st.svg',
				'/sites/vn_temp/flags/4x3/sv.svg',
				'/sites/vn_temp/flags/4x3/sx.svg',
				'/sites/vn_temp/flags/4x3/sy.svg',
				'/sites/vn_temp/flags/4x3/sz.svg',
				'/sites/vn_temp/flags/4x3/tc.svg',
				'/sites/vn_temp/flags/4x3/td.svg',
				'/sites/vn_temp/flags/4x3/tf.svg',
				'/sites/vn_temp/flags/4x3/tg.svg',
				'/sites/vn_temp/flags/4x3/th.svg',
				'/sites/vn_temp/flags/4x3/tj.svg',
				'/sites/vn_temp/flags/4x3/tk.svg',
				'/sites/vn_temp/flags/4x3/tl.svg',
				'/sites/vn_temp/flags/4x3/tm.svg',
				'/sites/vn_temp/flags/4x3/tn.svg',
				'/sites/vn_temp/flags/4x3/to.svg',
				'/sites/vn_temp/flags/4x3/tr.svg',
				'/sites/vn_temp/flags/4x3/tt.svg',
				'/sites/vn_temp/flags/4x3/tv.svg',
				'/sites/vn_temp/flags/4x3/tw.svg',
				'/sites/vn_temp/flags/4x3/tz.svg',
				'/sites/vn_temp/flags/4x3/ua.svg',
				'/sites/vn_temp/flags/4x3/ug.svg',
				'/sites/vn_temp/flags/4x3/um.svg',
				'/sites/vn_temp/flags/4x3/un.svg',
				'/sites/vn_temp/flags/4x3/us.svg',
				'/sites/vn_temp/flags/4x3/uy.svg',
				'/sites/vn_temp/flags/4x3/uz.svg',
				'/sites/vn_temp/flags/4x3/va.svg',
				'/sites/vn_temp/flags/4x3/vc.svg',
				'/sites/vn_temp/flags/4x3/ve.svg',
				'/sites/vn_temp/flags/4x3/vg.svg',
				'/sites/vn_temp/flags/4x3/vi.svg',
				'/sites/vn_temp/flags/4x3/vn.svg',
				'/sites/vn_temp/flags/4x3/vu.svg',
				'/sites/vn_temp/flags/4x3/wf.svg',
				'/sites/vn_temp/flags/4x3/ws.svg',
				'/sites/vn_temp/flags/4x3/ye.svg',
				'/sites/vn_temp/flags/4x3/yt.svg',
				'/sites/vn_temp/flags/4x3/za.svg',
				'/sites/vn_temp/flags/4x3/zm.svg',
				'/sites/vn_temp/flags/4x3/zw.svg',
				'/sites/vn_temp/images/15up_icon.jpg',
				'/sites/vn_temp/images/17up_icon.jpg',
				'/sites/vn_temp/images/18up_icon.jpg',
				'/sites/vn_temp/images/999_banner.jpg',
				'/sites/vn_temp/images/999_img1.jpg',
				'/sites/vn_temp/images/999_img2.jpg',
				'/sites/vn_temp/images/999_img3.jpg',
				'/sites/vn_temp/images/999_img4.jpg',
				'/sites/vn_temp/images/999_img5.jpg',
				'/sites/vn_temp/images/999_img6.jpg',
				'/sites/vn_temp/images/999_img7.jpg',
				'/sites/vn_temp/images/999_img8.jpg',
				'/sites/vn_temp/images/999_thumb.png',
				'/sites/vn_temp/images/999_thumb_lg.png',
				'/sites/vn_temp/images/999_wp.jpg',
				'/sites/vn_temp/images/AllAges_icon.jpg',
				'/sites/vn_temp/images/aloners_thumb.png',
				'/sites/vn_temp/images/amazon_button.png',
				'/sites/vn_temp/images/amnesia_thumb.png',
				'/sites/vn_temp/images/amnesia_thumb_lg.png',
				'/sites/vn_temp/images/android-chrome-192x192.png',
				'/sites/vn_temp/images/android-chrome-512x512.png',
				'/sites/vn_temp/images/aoishiro_thumb.png',
				'/sites/vn_temp/images/aoishiro_thumb_lg.png',
				'/sites/vn_temp/images/apple-touch-icon.png',
				'/sites/vn_temp/images/area_x_thumb.png',
				'/sites/vn_temp/images/aselia_thumb.png',
				'/sites/vn_temp/images/aselia_thumb_lg.png',
				'/sites/vn_temp/images/ayakashi_gohan_thumb.png',
				'/sites/vn_temp/images/a_kiss_for_the_petals_thumb.png',
				'/sites/vn_temp/images/a_kiss_for_the_petals_thumb_lg.png',
				'/sites/vn_temp/images/beyond_eden_thumb.png',
				'/sites/vn_temp/images/black_wolves_saga_thumb.png',
				'/sites/vn_temp/images/black_wolves_saga_thumb_lg.png',
				'/sites/vn_temp/images/browserconfig.xml',
				'/sites/vn_temp/images/bunny_black_thumb.png',
				'/sites/vn_temp/images/bunny_black_thumb_lg.png',
				'/sites/vn_temp/images/busters_img1.jpg',
				'/sites/vn_temp/images/busters_img10.jpg',
				'/sites/vn_temp/images/busters_img11.jpg',
				'/sites/vn_temp/images/busters_img12.jpg',
				'/sites/vn_temp/images/busters_img13.jpg',
				'/sites/vn_temp/images/busters_img2.jpg',
				'/sites/vn_temp/images/busters_img3.jpg',
				'/sites/vn_temp/images/busters_img4.jpg',
				'/sites/vn_temp/images/busters_img5.jpg',
				'/sites/vn_temp/images/busters_img6.jpg',
				'/sites/vn_temp/images/busters_img7.jpg',
				'/sites/vn_temp/images/busters_img8.jpg',
				'/sites/vn_temp/images/busters_img9.jpg',
				'/sites/vn_temp/images/busters_wp.png',
				'/sites/vn_temp/images/cage_open_thumb.png',
				'/sites/vn_temp/images/cage_open_vndb.png',
				'/sites/vn_temp/images/chaos_child_banner.png',
				'/sites/vn_temp/images/chaos_child_thumb.png',
				'/sites/vn_temp/images/chaos_child_thumb_lg.png',
				'/sites/vn_temp/images/chrono_clock_thumb.png',
				'/sites/vn_temp/images/chrono_clock_thumb_lg.png',
				'/sites/vn_temp/images/cinderella_phenomenon_thumb.png',
				'/sites/vn_temp/images/cinderella_phenomenon_thumb_lg.png',
				'/sites/vn_temp/images/clannad_banner.jpg',
				'/sites/vn_temp/images/clannad_thumb.png',
				'/sites/vn_temp/images/clannad_thumb_lg.png',
				'/sites/vn_temp/images/close.png',
				'/sites/vn_temp/images/code_realize_thumb.png',
				'/sites/vn_temp/images/code_realize_thumb_lg.png',
				'/sites/vn_temp/images/collar_x_malice_thumb.png',
				'/sites/vn_temp/images/collar_x_malice_thumb_lg.png',
				'/sites/vn_temp/images/coming_out_on_top_thumb.png',
				'/sites/vn_temp/images/comyu_thumb.png',
				'/sites/vn_temp/images/comyu_thumb_lg.png',
				'/sites/vn_temp/images/controls.png',
				'/sites/vn_temp/images/corpse_party_thumb.png',
				'/sites/vn_temp/images/daibanchou_thumb.png',
				'/sites/vn_temp/images/dandelion_thumb.png',
				'/sites/vn_temp/images/danganronpa_banner.png',
				'/sites/vn_temp/images/danganronpa_img1.jpg',
				'/sites/vn_temp/images/danganronpa_img2.jpg',
				'/sites/vn_temp/images/danganronpa_img3.jpg',
				'/sites/vn_temp/images/danganronpa_img4.jpg',
				'/sites/vn_temp/images/danganronpa_img5.jpg',
				'/sites/vn_temp/images/danganronpa_img6.jpg',
				'/sites/vn_temp/images/danganronpa_img7.jpg',
				'/sites/vn_temp/images/danganronpa_img8.jpg',
				'/sites/vn_temp/images/danganronpa_thumb.png',
				'/sites/vn_temp/images/danganronpa_thumb_lg.png',
				'/sites/vn_temp/images/danganronpa_wp.jpg',
				'/sites/vn_temp/images/denpasoft_button.png',
				'/sites/vn_temp/images/devil_on_g_string_thumb.png',
				'/sites/vn_temp/images/devil_on_g_string_thumb_lg.png',
				'/sites/vn_temp/images/dies_irae.jpg',
				'/sites/vn_temp/images/dies_irae_thumb.png',
				'/sites/vn_temp/images/dies_irae_thumb_lg.png',
				'/sites/vn_temp/images/dracu_riot_thumb.png',
				'/sites/vn_temp/images/dracu_riot_thumb_lg.png',
				'/sites/vn_temp/images/dramatical_murder_thumb.png',
				'/sites/vn_temp/images/dramatical_murder_thumb_lg.png',
				'/sites/vn_temp/images/eden_thumb.png',
				'/sites/vn_temp/images/eden_thumb_lg.png',
				'/sites/vn_temp/images/ef_thumb.png',
				'/sites/vn_temp/images/ef_thumb_lg.png',
				'/sites/vn_temp/images/eien_no_aselia_thumb.png',
				'/sites/vn_temp/images/eiyuu_senki_thumb.png',
				'/sites/vn_temp/images/eiyuu_senki_thumb_lg.png',
				'/sites/vn_temp/images/evenicle_thumb.png',
				'/sites/vn_temp/images/evenicle_thumb_lg.png',
				'/sites/vn_temp/images/ever17_thumb.png',
				'/sites/vn_temp/images/fate_stay_night_thumb.png',
				'/sites/vn_temp/images/fate_stay_night_thumb_lg.png',
				'/sites/vn_temp/images/fault_milestone_thumb.png',
				'/sites/vn_temp/images/fault_milestone_thumb_lg.png',
				'/sites/vn_temp/images/favicon-16x16.png',
				'/sites/vn_temp/images/favicon-32x32.png',
				'/sites/vn_temp/images/flowers_thumb.png',
				'/sites/vn_temp/images/flowers_thumb_lg.png',
				'/sites/vn_temp/images/fureraba_thumb.png',
				'/sites/vn_temp/images/fureraba_thumb_lg.png',
				'/sites/vn_temp/images/galaxy_angel_thumb.png',
				'/sites/vn_temp/images/girlish_grimoire_thumb.png',
				'/sites/vn_temp/images/gog_button.png',
				'/sites/vn_temp/images/grisaia_banner.jpg',
				'/sites/vn_temp/images/grisaia_thumb.png',
				'/sites/vn_temp/images/grisaia_thumb_lg.png',
				'/sites/vn_temp/images/hakuisei_thumb.png',
				'/sites/vn_temp/images/hatoful_boyfriend_thumb.png',
				'/sites/vn_temp/images/hatoful_boyfriend_thumb_lg.png',
				'/sites/vn_temp/images/heart_no_kuni_no_alice_thumb.png',
				'/sites/vn_temp/images/heart_no_kuni_no_alice_thumb_lg.png',
				'/sites/vn_temp/images/her_tears_were_my_light_thumb.png',
				'/sites/vn_temp/images/hifm.jpg',
				'/sites/vn_temp/images/hifm_thumb.png',
				'/sites/vn_temp/images/hifm_thumb_lg.png',
				'/sites/vn_temp/images/highway_blossoms_thumb.png',
				'/sites/vn_temp/images/highway_blossoms_thumb_lg.png',
				'/sites/vn_temp/images/higurashi.jpg',
				'/sites/vn_temp/images/higurashi_banner.jpg',
				'/sites/vn_temp/images/higurashi_thumb.png',
				'/sites/vn_temp/images/higurashi_thumb_lg.png',
				'/sites/vn_temp/images/himawari_thumb.png',
				'/sites/vn_temp/images/himawari_thumb_lg.png',
				'/sites/vn_temp/images/hoshizora_thumb.png',
				'/sites/vn_temp/images/hoshizora_thumb_lg.png',
				'/sites/vn_temp/images/ijiwaru_thumb.png',
				'/sites/vn_temp/images/itch_button.png',
				'/sites/vn_temp/images/jast_button.png',
				'/sites/vn_temp/images/jlist_button.png',
				'/sites/vn_temp/images/kamidori_thumb.png',
				'/sites/vn_temp/images/kamidori_thumb_lg.png',
				'/sites/vn_temp/images/kara_no_shoujo_banner.png',
				'/sites/vn_temp/images/kara_no_shoujo_thumb.png',
				'/sites/vn_temp/images/kara_no_shoujo_thumb_lg.png',
				'/sites/vn_temp/images/Katawa_Shoujo_choices_menu.png',
				'/sites/vn_temp/images/katawa_shoujo_thumb.png',
				'/sites/vn_temp/images/katawa_shoujo_thumb_lg.png',
				'/sites/vn_temp/images/kindred_spirits_thumb.png',
				'/sites/vn_temp/images/kindred_spirits_thumb_lg.png',
				'/sites/vn_temp/images/kira_kira_thumb.png',
				'/sites/vn_temp/images/konosora_thumb.png',
				'/sites/vn_temp/images/konosora_thumb_lg.png',
				'/sites/vn_temp/images/lamento_thumb.png',
				'/sites/vn_temp/images/lamento_thumb_lg.png',
				'/sites/vn_temp/images/lb_banner.jpg',
				'/sites/vn_temp/images/little_busters_thumb.png',
				'/sites/vn_temp/images/little_busters_thumb_lg.png',
				'/sites/vn_temp/images/loading.gif',
				'/sites/vn_temp/images/majikoi_a2_thumb.png',
				'/sites/vn_temp/images/majikoi_s_thumb.png',
				'/sites/vn_temp/images/majikoi_thumb.png',
				'/sites/vn_temp/images/majikoi_thumb_lg.png',
				'/sites/vn_temp/images/mangagamer_button.png',
				'/sites/vn_temp/images/mla.jpg',
				'/sites/vn_temp/images/mla_thumb.png',
				'/sites/vn_temp/images/mla_thumb_lg.png',
				'/sites/vn_temp/images/monster_girl_quest_thumb.png',
				'/sites/vn_temp/images/monster_girl_quest_thumb_lg.png',
				'/sites/vn_temp/images/mstile-150x150.png',
				'/sites/vn_temp/images/muv_luv_thumb.png',
				'/sites/vn_temp/images/muv_luv_thumb_lg.png',
				'/sites/vn_temp/images/mystic_messenger_thumb.png',
				'/sites/vn_temp/images/mystic_messenger_thumb_lg.png',
				'/sites/vn_temp/images/nameless_thumb.png',
				'/sites/vn_temp/images/nameless_thumb_lg.png',
				'/sites/vn_temp/images/narcissu_thumb.png',
				'/sites/vn_temp/images/narcissu_thumb_lg.png',
				'/sites/vn_temp/images/next.png',
				'/sites/vn_temp/images/nightshade_thumb.png',
				'/sites/vn_temp/images/nightshade_thumb_lg.png',
				'/sites/vn_temp/images/no_thank_you_thumb.png',
				'/sites/vn_temp/images/no_thank_you_thumb_lg.png',
				'/sites/vn_temp/images/osadai_thumb.png',
				'/sites/vn_temp/images/osadai_thumb_lg.png',
				'/sites/vn_temp/images/phoenixWright_banner.jpg',
				'/sites/vn_temp/images/phoenix_wright_img1.jpg',
				'/sites/vn_temp/images/phoenix_wright_img2.jpg',
				'/sites/vn_temp/images/phoenix_wright_img3.jpg',
				'/sites/vn_temp/images/phoenix_wright_img4.jpg',
				'/sites/vn_temp/images/phoenix_wright_img5.jpg',
				'/sites/vn_temp/images/phoenix_wright_img6.jpg',
				'/sites/vn_temp/images/phoenix_wright_img7.jpg',
				'/sites/vn_temp/images/phoenix_wright_img8.jpg',
				'/sites/vn_temp/images/phoenix_wright_thumb.png',
				'/sites/vn_temp/images/phoenix_wright_thumb_lg.png',
				'/sites/vn_temp/images/phoenix_wright_wp.jpg',
				'/sites/vn_temp/images/planetarian_thumb.png',
				'/sites/vn_temp/images/planetarian_thumb_lg.png',
				'/sites/vn_temp/images/prev.png',
				'/sites/vn_temp/images/princess_evangile_thumb.png',
				'/sites/vn_temp/images/princess_evangile_thumb_lg.png',
				'/sites/vn_temp/images/quartett_thumb.png',
				'/sites/vn_temp/images/rance_vi_thumb.png',
				'/sites/vn_temp/images/rance_vi_thumb_lg.png',
				'/sites/vn_temp/images/reddit_button.png',
				'/sites/vn_temp/images/reddit_head_ico.png',
				'/sites/vn_temp/images/rewrite_banner.jpg',
				'/sites/vn_temp/images/rewrite_thumb.png',
				'/sites/vn_temp/images/rewrite_thumb_lg.png',
				'/sites/vn_temp/images/rightstuf_button.png',
				'/sites/vn_temp/images/root_double_banner.jpg',
				'/sites/vn_temp/images/root_double_thumb.png',
				'/sites/vn_temp/images/root_double_thumb_lg.png',
				'/sites/vn_temp/images/rose_gun_days_thumb.png',
				'/sites/vn_temp/images/rose_gun_days_thumb_lg.png',
				'/sites/vn_temp/images/safari-pinned-tab.svg',
				'/sites/vn_temp/images/saya_no_uta_thumb.png',
				'/sites/vn_temp/images/saya_no_uta_thumb_lg.png',
				'/sites/vn_temp/images/seabed_thumb.png',
				'/sites/vn_temp/images/seabed_thumb_lg.png',
				'/sites/vn_temp/images/sekien_no_inganock_thumb.png',
				'/sites/vn_temp/images/sekien_no_inganock_thumb_lg.png',
				'/sites/vn_temp/images/sengoku_rance_thumb.png',
				'/sites/vn_temp/images/sengoku_rance_thumb_lg.png',
				'/sites/vn_temp/images/sharin_no_kuni_thumb.png',
				'/sites/vn_temp/images/sharin_no_kuni_thumb_lg.png',
				'/sites/vn_temp/images/shoujo_img1.jpg',
				'/sites/vn_temp/images/shoujo_img10.jpg',
				'/sites/vn_temp/images/shoujo_img11.jpg',
				'/sites/vn_temp/images/shoujo_img12.jpg',
				'/sites/vn_temp/images/shoujo_img13.jpg',
				'/sites/vn_temp/images/shoujo_img2.jpg',
				'/sites/vn_temp/images/shoujo_img3.jpg',
				'/sites/vn_temp/images/shoujo_img4.jpg',
				'/sites/vn_temp/images/shoujo_img5.jpg',
				'/sites/vn_temp/images/shoujo_img6.jpg',
				'/sites/vn_temp/images/shoujo_img7.jpg',
				'/sites/vn_temp/images/shoujo_img8.jpg',
				'/sites/vn_temp/images/shoujo_img9.jpg',
				'/sites/vn_temp/images/shoujo_wp.png',
				'/sites/vn_temp/images/site.webmanifest',
				'/sites/vn_temp/images/sky_full_of_stars_thumb.png',
				'/sites/vn_temp/images/snoo.png',
				'/sites/vn_temp/images/steam_button.png',
				'/sites/vn_temp/images/steins_gate_banner.jpg',
				'/sites/vn_temp/images/steins_gate_img1.jpg',
				'/sites/vn_temp/images/steins_gate_img2.jpg',
				'/sites/vn_temp/images/steins_gate_img3.jpg',
				'/sites/vn_temp/images/steins_gate_img4.jpg',
				'/sites/vn_temp/images/steins_gate_img5.jpg',
				'/sites/vn_temp/images/steins_gate_img6.jpg',
				'/sites/vn_temp/images/steins_gate_img7.jpg',
				'/sites/vn_temp/images/steins_gate_img8.jpg',
				'/sites/vn_temp/images/steins_gate_thumb.png',
				'/sites/vn_temp/images/steins_gate_thumb_lg.png',
				'/sites/vn_temp/images/steins_gate_wp.png',
				'/sites/vn_temp/images/subahibi_thumb.png',
				'/sites/vn_temp/images/subahibi_thumb_lg.png',
				'/sites/vn_temp/images/swan_song_thumb.png',
				'/sites/vn_temp/images/swan_song_thumb_lg.png',
				'/sites/vn_temp/images/symphonic_rain_thumb.png',
				'/sites/vn_temp/images/symphonic_rain_thumb_lg.png',
				'/sites/vn_temp/images/the_confines_of_the_crown_thumb.png',
				'/sites/vn_temp/images/the_second_reproduction_thumb.png',
				'/sites/vn_temp/images/togainu_no_chi_thumb.png',
				'/sites/vn_temp/images/togainu_no_chi_thumb_lg.png',
				'/sites/vn_temp/images/tokyo_babel_thumb.png',
				'/sites/vn_temp/images/tokyo_babel_thumb_lg.png',
				'/sites/vn_temp/images/tsujidou_thumb.png',
				'/sites/vn_temp/images/tsujidou_thumb_lg.png',
				'/sites/vn_temp/images/tsukihime_thumb.png',
				'/sites/vn_temp/images/tsukihime_thumb_lg.png',
				'/sites/vn_temp/images/umineko_thumb.png',
				'/sites/vn_temp/images/umineko_thumb_lg.png',
				'/sites/vn_temp/images/utawarerumono_thumb.png',
				'/sites/vn_temp/images/utawarerumono_thumb_lg.png',
				'/sites/vn_temp/images/vallhalla_thumb.png',
				'/sites/vn_temp/images/vallhalla_thumb_lg.png',
				'/sites/vn_temp/images/vlr_thumb.png',
				'/sites/vn_temp/images/vndb_button.png',
				'/sites/vn_temp/images/website_button.png',
				'/sites/vn_temp/images/your_heart_thumb.png',
				'/sites/vn_temp/images/yuno_thumb.png',
				'/sites/vn_temp/images/yuno_thumb_lg.png',
				'/sites/vn_temp/js/bootstrap.js',
				'/sites/vn_temp/js/bootstrap.min.js',
				'/sites/vn_temp/js/fakeloader.min.js',
				'/sites/vn_temp/js/flickity.pkgd.min.js',
				'/sites/vn_temp/js/jquery-3.3.1.min.js',
				'/sites/vn_temp/js/jquery.jcarousel.min.js',
				'/sites/vn_temp/js/lazysizes.min.js',
				'/sites/vn_temp/js/ls.unveilhooks.min.js',
				'/sites/vn_temp/js/npm.js',
			]);
    	})
		.then(function() {
			console.log('WORKER: install complete');
		})
	);
});

// https://css-tricks.com/serviceworker-for-offline/
// NICOLAS BEVACQUA ON NOVEMBER 10, 2015
self.addEventListener('fetch', function(event) {
	//console.log('WORKER: fetch started')

	// Fix by Paul Irish for Chromium dev tools bug generating errors
	if (event.request.cache === 'only-if-cached' && event.request.mode !== 'same-origin') {
		return;
	}
	if (event.request.method !== 'GET') {
		console.log('WORKER: fetch ignored', event.request.method, event.request.url);
		return;
	}

	event.respondWith(
		caches.match(event.request).then(function(cached) {
			var netReq = fetch(event.request)
				.then(fetchedFromNetwork, unableToResolve)
				.catch(unableToResolve);

			console.log('WORKER: fetch event', cached ? '(cached)' : '(network)', event.request.url);
			return cached || netReq; // return true if we have a cached or networked match

			function fetchedFromNetwork(repsonse) {
				var cacheCopy = response.clone();

				console.log('WORKER: fetch response from network', event.request.url);

				caches.open(version + 'pages').then(function add(cache) {
					cache.put(event.request, cacheCopy);
				})
				.then(function() {
					console.log('WORKER: fetch response stored in cache', event.request.url);
				});

				return response;
			}

			function unableToResolve() {
				console.log('WORKER: fetch request from both cache and network failed');

				return caches.match('/sites/vn_temp/index.html');
			}
		})
	);
});

self.addEventListener('activate', function(event) {
	//console.log('WORKER: activation in progress');

	event.waitUntil(
		caches.keys().then(function(keys) {
			return Promise.all(
				keys.filter(function(key) {
					return !key.startsWith(version);
				}).map(function(key) {
					return caches.delete(key);
				})
			);
		})
		.then(function() {
			console.log('WORKER: activation complete');
		})
	);
});
