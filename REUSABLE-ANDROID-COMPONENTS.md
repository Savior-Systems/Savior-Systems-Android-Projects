# Savior Systems: Reusable Android Components

Since we are publishing 30 apps, we use a copy-paste standard component pattern to ensure clean codebase isolation (avoiding Google's repetitive content flags) while maintaining developer velocity.

---

## 1. Unified AdManager

Every app uses this singleton to manage the lifecycle of banner and interstitial ads.

```kotlin
package com.saviorsystems.core.ads

import android.app.Activity
import android.content.Context
import android.util.Log
import com.google.android.gms.ads.AdRequest
import com.google.android.gms.ads.LoadAdError
import com.google.android.gms.ads.interstitial.InterstitialAd
import com.google.android.gms.ads.interstitial.InterstitialAdLoadCallback

object AdManager {
    private const val TAG = "AdManager"
    private var mInterstitialAd: InterstitialAd? = null
    private var lastInterstitialShowTime: Long = 0
    private const val COOLDOWN_MILLIS = 180_000L // 3-minute frequency cap

    fun loadInterstitial(context: Context, adUnitId: String) {
        if (mInterstitialAd != null) return
        
        val adRequest = AdRequest.Builder().build()
        InterstitialAd.load(context, adUnitId, adRequest, object : InterstitialAdLoadCallback() {
            override fun onAdFailedToLoad(adError: LoadAdError) {
                Log.d(TAG, "Ad failed to load: ${adError.message}")
                mInterstitialAd = null
            }

            override fun onAdLoaded(interstitialAd: InterstitialAd) {
                Log.d(TAG, "Ad loaded successfully.")
                mInterstitialAd = interstitialAd
            }
        })
    }

    fun showInterstitial(activity: Activity, adUnitId: String, onAdDismissed: () -> Unit) {
        val currentTime = System.currentTimeMillis()
        val timeDiff = currentTime - lastInterstitialShowTime

        if (mInterstitialAd != null && timeDiff >= COOLDOWN_MILLIS) {
            mInterstitialAd?.fullScreenContentCallback = object : com.google.android.gms.ads.FullScreenContentCallback() {
                override fun onAdDismissedFullScreenContent() {
                    Log.d(TAG, "Ad dismissed. Preloading next one.")
                    mInterstitialAd = null
                    lastInterstitialShowTime = System.currentTimeMillis()
                    onAdDismissed()
                    loadInterstitial(activity, adUnitId)
                }

                override fun onAdFailedToShowFullScreenContent(adError: com.google.android.gms.ads.AdError) {
                    Log.d(TAG, "Ad failed to show: ${adError.message}")
                    mInterstitialAd = null
                    onAdDismissed()
                }
            }
            mInterstitialAd?.show(activity)
        } else {
            Log.d(TAG, "Ad skipped. Cooldown active or ad not ready yet.")
            onAdDismissed()
            if (mInterstitialAd == null) {
                loadInterstitial(activity, adUnitId)
            }
        }
    }
}
```

---

## 2. Dynamic Theme Setup

To pass Play Console reviews, we configure color definitions using distinct material themes.

```kotlin
package com.saviorsystems.core.theme

import android.os.Build
import androidx.compose.foundation.isSystemInDarkTheme
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.darkColorScheme
import androidx.compose.material3.dynamicDarkColorScheme
import androidx.compose.material3.dynamicLightColorScheme
import androidx.compose.material3.lightColorScheme
import androidx.compose.runtime.Composable
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.platform.LocalContext

// Customize these colors for each app to remain distinct
val LightPrimary = Color(0xFF6750A4)
val LightSecondary = Color(0xFF625B71)
val DarkPrimary = Color(0xFFD0BCFF)
val DarkSecondary = Color(0xFFCCC2DC)

private val DarkColorScheme = darkColorScheme(
    primary = DarkPrimary,
    secondary = DarkSecondary
)

private val LightColorScheme = lightColorScheme(
    primary = LightPrimary,
    secondary = LightSecondary
)

@Composable
fun AppTheme(
    darkTheme: Boolean = isSystemInDarkTheme(),
    dynamicColor: Boolean = true,
    content: @Composable () -> Unit
) {
    val colorScheme = when {
        dynamicColor && Build.VERSION.SDK_INT >= Build.VERSION_CODES_S -> {
            val context = LocalContext.current
            if (darkTheme) dynamicDarkColorScheme(context) else dynamicLightColorScheme(context)
        }
        darkTheme -> DarkColorScheme
        else -> LightColorScheme
    }

    MaterialTheme(
        colorScheme = colorScheme,
        content = content
    )
}
```

---

## 3. General Settings Screen Composable

We use a standard, modular Settings UI structure in Compose.

```kotlin
package com.saviorsystems.core.ui

import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.*
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Info
import androidx.compose.material.icons.filled.Lock
import androidx.compose.material.icons.filled.Share
import androidx.compose.material.icons.filled.Star
import androidx.compose.material3.*
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.vector.ImageVector
import androidx.compose.ui.unit.dp

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun SettingsScreen(
    appVersion: String,
    onPrivacyPolicyClick: () -> Unit,
    onRateAppClick: () -> Unit,
    onShareAppClick: () -> Unit,
    onAboutClick: () -> Unit
) {
    Scaffold(
        topBar = { TopAppBar(title = { Text("Settings") }) }
    ) { paddingValues ->
        Column(
            modifier = Modifier
                .fillMaxSize()
                .padding(paddingValues)
                .padding(16.dp),
            verticalArrangement = Arrangement.spacedBy(8.dp)
        ) {
            SettingsItem(icon = Icons.Default.Lock, title = "Privacy Policy", onClick = onPrivacyPolicyClick)
            SettingsItem(icon = Icons.Default.Star, title = "Rate Application", onClick = onRateAppClick)
            SettingsItem(icon = Icons.Default.Share, title = "Share with Friends", onClick = onShareAppClick)
            SettingsItem(icon = Icons.Default.Info, title = "About Application", onClick = onAboutClick)
            
            Spacer(modifier = Modifier.weight(1f))
            
            Text(
                text = "Version: $appVersion",
                style = MaterialTheme.typography.bodySmall,
                modifier = Modifier.align(Alignment.CenterHorizontally),
                color = MaterialTheme.colorScheme.onSurfaceVariant
            )
        }
    }
}

@Composable
fun SettingsItem(icon: ImageVector, title: String, onClick: () -> Unit) {
    Row(
        modifier = Modifier
            .fillMaxWidth()
            .clickable(onClick = onClick)
            .padding(vertical = 12.dp, horizontal = 8.dp),
        verticalAlignment = Alignment.CenterVertically,
        horizontalArrangement = Arrangement.spacedBy(16.dp)
    ) {
        Icon(imageVector = icon, contentDescription = title, tint = MaterialTheme.colorScheme.primary)
        Text(text = title, style = MaterialTheme.typography.bodyLarge)
    }
}
```
