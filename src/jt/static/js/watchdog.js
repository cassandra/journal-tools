(function() {

    window.Jt = window.Jt || {};

    const MODULE_NAME = 'watchdog';    

    const JtWatchdog = {
        add: function( type, initFunction, normalRefreshMs ) {
            watchdogAdd( type, initFunction, normalRefreshMs );
        },
        ok: function( type ) {
            watchdogOk( type );
        }
    };

    window.Jt.watchdog = JtWatchdog;

    /*
      WATCHDOG

      - Provides backup to ensure periodic background queries keep running.
    */

    const TRACE = false;
    
    var WatchdogTimers = {};
    var watchdogInactive = {};
    var watchdogFunctions = {};

    function watchdogAdd( type, initFunction, normalRefreshMs ) {
        watchdogInactive[type] = false;
        watchdogFunctions[type] = initFunction;
        WatchdogTimers[type] = setInterval( function() { watchdogCheck( type ); },
                                            2 * normalRefreshMs );
    }
    
    function watchdogCheck( type ) {
        if ( ! ( type in watchdogInactive )) {
            console.error( `No watchdog timer added for "${type}". Cannot check.`);
            return;
        }
        
        if ( Jt.DEBUG && TRACE ) { console.debug( `Watchdog check: ${type}` ); }
        if ( watchdogInactive[type] ) {
            if ( Jt.DEBUG ) { console.debug( `Watchdog detected "${type}" stopped. Restarting.` ); }
            watchdogFunctions[type]();
            watchdogInactive[type] = false;

        } else {
            watchdogInactive[type] = true;
        }
    }
    
    //--------------------
    function watchdogOk( type ) {
        watchdogInactive[type] = false;
    }
    
})();
